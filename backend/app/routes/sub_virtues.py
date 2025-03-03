from fastapi import APIRouter, HTTPException, status
from bson.objectid import ObjectId
from typing import List

from app.models.schemas import SubvirtueCreate
from app.database.mongodb import subvirtues, main_virtues, weaknesses, questions

router = APIRouter()


@router.delete("/subvirtues/super-delete")
async def super_delete_subvirtues():
    try:
        await subvirtues.delete_many({})
        return {"status": "all deleted"}
    except:
        raise HTTPException(status_code=400, detail="Failed to delete")


# Sub-virtues endpoints
@router.post("/subvirtues/")
async def create_subvirtue(subvirtue: SubvirtueCreate):
    # Validate item_code format for subvirtues
    parts = subvirtue.item_code.split(".")
    if len(parts) != 3 or not all(part.isdigit() for part in parts):
        raise HTTPException(
            status_code=400, detail="Invalid item code format for subvirtues"
        )

    # Check if item_code already exists in any collection
    if (
        await main_virtues.find_one({"item_code": subvirtue.item_code})
        or await weaknesses.find_one({"item_code": subvirtue.item_code})
        or await subvirtues.find_one({"item_code": subvirtue.item_code})
        or await questions.find_one({"item_code": subvirtue.item_code})
    ):
        raise HTTPException(status_code=400, detail="Item code already exists")

    try:
        # Check if main virtue exists
        main_virtue = await main_virtues.find_one(
            {"_id": ObjectId(subvirtue.main_virtue_id)}
        )
        if not main_virtue:
            raise HTTPException(status_code=404, detail="Main virtue not found")

        # Ensure subvirtue's item_code matches the main virtue's first part
        main_virtue_parts = main_virtue["item_code"].split(".")
        if parts[0] != main_virtue_parts[0]:
            raise HTTPException(
                status_code=400, detail="Invalid item code for subvirtue"
            )

        new_subvirtue = subvirtue.dict()

        result = await subvirtues.insert_one(new_subvirtue)
        created_subvirtue = await subvirtues.find_one({"_id": result.inserted_id})
        created_subvirtue["_id"] = str(created_subvirtue["_id"])
        return created_subvirtue
    except Exception as e:
        if "Invalid ID format" in str(e):
            raise e
        raise HTTPException(status_code=400, detail="Invalid main_virtue_id format")


# Modify the update_subvirtue function
@router.put("/subvirtues/{subvirtue_id}")
async def update_subvirtue(subvirtue_id: str, subvirtue_data: SubvirtueCreate):
    try:
        # Check if item_code already exists for another document in any collection
        if (
            await main_virtues.find_one({"item_code": subvirtue_data.item_code})
            or await weaknesses.find_one({"item_code": subvirtue_data.item_code})
            or await subvirtues.find_one(
                {
                    "item_code": subvirtue_data.item_code,
                    "_id": {"$ne": ObjectId(subvirtue_id)},
                }
            )
            or await questions.find_one({"item_code": subvirtue_data.item_code})
        ):
            raise HTTPException(status_code=400, detail="Item code already exists")

        # Validate item_code format for subvirtues
        parts = subvirtue_data.item_code.split(".")
        if len(parts) != 3 or not all(part.isdigit() for part in parts):
            raise HTTPException(
                status_code=400, detail="Invalid item code format for subvirtues"
            )

        # Check if main virtue exists
        try:
            main_virtue = await main_virtues.find_one(
                {"_id": ObjectId(subvirtue_data.main_virtue_id)}
            )
            if not main_virtue:
                raise HTTPException(status_code=404, detail="Main virtue not found")
        except:
            raise HTTPException(status_code=400, detail="Invalid main_virtue_id format")

        # Ensure subvirtue's item_code matches the main virtue's first part
        main_virtue_parts = main_virtue["item_code"].split(".")
        if parts[0] != main_virtue_parts[0]:
            raise HTTPException(
                status_code=400, detail="Invalid item code for subvirtue"
            )

        update_data = subvirtue_data.dict()

        await subvirtues.update_one(
            {"_id": ObjectId(subvirtue_id)}, {"$set": update_data}
        )

        updated_subvirtue = await subvirtues.find_one({"_id": ObjectId(subvirtue_id)})
        if not updated_subvirtue:
            raise HTTPException(status_code=404, detail="Subvirtue not found")

        updated_subvirtue["_id"] = str(updated_subvirtue["_id"])
        return updated_subvirtue
    except Exception as e:
        if "Invalid main_virtue_id format" in str(e) or "Main virtue not found" in str(
            e
        ):
            raise e
        raise HTTPException(status_code=400, detail="Invalid ID format")


@router.get("/subvirtues/")
async def get_all_subvirtues():
    subvirtue_list = await subvirtues.find().to_list(1000)

    # Convert ObjectIds to strings and add main virtue information
    for sv in subvirtue_list:
        sv["_id"] = str(sv["_id"])
        try:
            main_virtue = await main_virtues.find_one(
                {"_id": ObjectId(sv["main_virtue_id"])}
            )
            if main_virtue:
                main_virtue["_id"] = str(main_virtue["_id"])
                sv["main_virtue"] = main_virtue
        except:
            sv["main_virtue"] = None

    return subvirtue_list


@router.get("/subvirtues/{subvirtue_id}")
async def get_subvirtue(subvirtue_id: str):
    try:
        subvirtue = await subvirtues.find_one({"_id": ObjectId(subvirtue_id)})
        if not subvirtue:
            raise HTTPException(status_code=404, detail="Subvirtue not found")

        subvirtue["_id"] = str(subvirtue["_id"])

        # Get main virtue data
        try:
            main_virtue = await main_virtues.find_one(
                {"_id": ObjectId(subvirtue["main_virtue_id"])}
            )
            if main_virtue:
                main_virtue["_id"] = str(main_virtue["_id"])
                subvirtue["main_virtue"] = main_virtue
        except:
            subvirtue["main_virtue"] = None

        return subvirtue
    except:
        raise HTTPException(status_code=400, detail="Invalid ID format")


@router.put("/subvirtues/{subvirtue_id}")
async def update_subvirtue(subvirtue_id: str, subvirtue_data: SubvirtueCreate):
    try:
        # Check if item_code already exists for another document in any collection
        if (
            await main_virtues.find_one({"item_code": subvirtue_data.item_code})
            or await weaknesses.find_one({"item_code": subvirtue_data.item_code})
            or await subvirtues.find_one(
                {
                    "item_code": subvirtue_data.item_code,
                    "_id": {"$ne": ObjectId(subvirtue_id)},
                }
            )
            or await questions.find_one({"item_code": subvirtue_data.item_code})
        ):
            raise HTTPException(status_code=400, detail="Item code already exists")

        # Validate item_code format for subvirtues
        parts = subvirtue_data.item_code.split(".")
        if (
            len(parts) != 3
            or not all(part.isdigit() for part in parts[0:2])
            or parts[2] != "0"
        ):
            raise HTTPException(
                status_code=400, detail="Invalid item code format for subvirtues"
            )

        # Check if main virtue exists
        try:
            main_virtue = await main_virtues.find_one(
                {"_id": ObjectId(subvirtue_data.main_virtue_id)}
            )
            if not main_virtue:
                raise HTTPException(status_code=404, detail="Main virtue not found")
        except:
            raise HTTPException(status_code=400, detail="Invalid main_virtue_id format")

        # Ensure subvirtue's item_code matches the main virtue's first part
        main_virtue_parts = main_virtue["item_code"].split(".")
        if parts[0] != main_virtue_parts[0]:
            raise HTTPException(
                status_code=400, detail="Invalid item code for subvirtue"
            )

        update_data = subvirtue_data.dict()

        await subvirtues.update_one(
            {"_id": ObjectId(subvirtue_id)}, {"$set": update_data}
        )

        updated_subvirtue = await subvirtues.find_one({"_id": ObjectId(subvirtue_id)})
        if not updated_subvirtue:
            raise HTTPException(status_code=404, detail="Subvirtue not found")

        updated_subvirtue["_id"] = str(updated_subvirtue["_id"])
        return updated_subvirtue
    except Exception as e:
        if "Invalid main_virtue_id format" in str(e) or "Main virtue not found" in str(
            e
        ):
            raise e
        raise HTTPException(status_code=400, detail="Invalid ID format")


@router.delete("/subvirtues/{subvirtue_id}")
async def delete_subvirtue(subvirtue_id: str):
    try:
        # Check if any weakness or question references this subvirtue
        if await weaknesses.find_one(
            {"suggested_subvirtue_ids": subvirtue_id}
        ) or await questions.find_one({"subvirtue_id": subvirtue_id}):
            raise HTTPException(
                status_code=400,
                detail="Cannot delete subvirtue with referenced weaknesses or questions",
            )

        result = await subvirtues.delete_one({"_id": ObjectId(subvirtue_id)})
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Subvirtue not found")
        return {"status": "deleted"}
    except:
        raise HTTPException(status_code=400, detail="Invalid ID format")
