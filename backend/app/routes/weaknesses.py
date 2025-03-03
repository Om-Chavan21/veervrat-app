from fastapi import APIRouter, HTTPException, status, Query
from bson.objectid import ObjectId
from typing import List, Optional

from app.models.schemas import WeaknessCreate
from app.database.mongodb import weaknesses, subvirtues, main_virtues, questions

router = APIRouter()


@router.delete("/weaknesses/super-delete")
async def super_delete_weaknesses():
    try:
        await weaknesses.delete_many({})
        return {"status": "all deleted"}
    except:
        raise HTTPException(status_code=400, detail="Failed to delete")


@router.post("/weaknesses/")
async def create_weakness(weakness: WeaknessCreate):
    # Validate item_code format for weaknesses
    if not weakness.item_code.startswith("W") or not weakness.item_code[1:].isdigit():
        raise HTTPException(
            status_code=400, detail="Invalid item code format for weaknesses"
        )

    # Check if item_code already exists in any collection
    if (
        await main_virtues.find_one({"item_code": weakness.item_code})
        or await weaknesses.find_one({"item_code": weakness.item_code})
        or await subvirtues.find_one({"item_code": weakness.item_code})
        or await questions.find_one({"item_code": weakness.item_code})
    ):
        raise HTTPException(status_code=400, detail="Item code already exists")

    try:
        # Validate subvirtue IDs
        for sv_id in weakness.suggested_subvirtue_ids:
            try:
                subvirtue = await subvirtues.find_one({"_id": ObjectId(sv_id)})
                if not subvirtue:
                    raise HTTPException(
                        status_code=404, detail=f"Subvirtue with ID {sv_id} not found"
                    )
            except:
                raise HTTPException(
                    status_code=400, detail=f"Invalid subvirtue ID format: {sv_id}"
                )

        new_weakness = weakness.dict()

        result = await weaknesses.insert_one(new_weakness)
        created_weakness = await weaknesses.find_one({"_id": result.inserted_id})
        created_weakness["_id"] = str(created_weakness["_id"])
        return created_weakness
    except Exception as e:
        if "Invalid subvirtue ID format" in str(e) or "not found" in str(e):
            raise e
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/weaknesses/")
async def get_all_weaknesses(group: Optional[str] = Query(None)):
    query = {}
    if group:
        query["group"] = group

    weakness_list = await weaknesses.find(query).to_list(1000)

    # Convert ObjectIds and add subvirtue information
    for weakness in weakness_list:
        weakness["_id"] = str(weakness["_id"])

        subvirtue_list = []
        for sv_id in weakness["suggested_subvirtue_ids"]:
            try:
                subvirtue = await subvirtues.find_one({"_id": ObjectId(sv_id)})
                if subvirtue:
                    subvirtue["_id"] = str(subvirtue["_id"])
                    subvirtue_list.append(subvirtue)
            except:
                pass

        weakness["suggested_subvirtues"] = subvirtue_list

    return weakness_list


@router.get("/weaknesses/{weakness_id}")
async def get_weakness(weakness_id: str):
    try:
        weakness = await weaknesses.find_one({"_id": ObjectId(weakness_id)})
        if not weakness:
            raise HTTPException(status_code=404, detail="Weakness not found")

        weakness["_id"] = str(weakness["_id"])

        # Get subvirtue data
        subvirtue_list = []
        for sv_id in weakness["suggested_subvirtue_ids"]:
            try:
                subvirtue = await subvirtues.find_one({"_id": ObjectId(sv_id)})
                if subvirtue:
                    subvirtue["_id"] = str(subvirtue["_id"])
                    subvirtue_list.append(subvirtue)
            except:
                pass

        weakness["suggested_subvirtues"] = subvirtue_list
        return weakness
    except:
        raise HTTPException(status_code=400, detail="Invalid ID format")


@router.put("/weaknesses/{weakness_id}")
async def update_weakness(weakness_id: str, weakness_data: WeaknessCreate):
    try:
        # Check if item_code already exists for another document in any collection
        if (
            await main_virtues.find_one({"item_code": weakness_data.item_code})
            or await weaknesses.find_one(
                {
                    "item_code": weakness_data.item_code,
                    "_id": {"$ne": ObjectId(weakness_id)},
                }
            )
            or await subvirtues.find_one({"item_code": weakness_data.item_code})
            or await questions.find_one({"item_code": weakness_data.item_code})
        ):
            raise HTTPException(status_code=400, detail="Item code already exists")

        # Validate item_code format for weaknesses
        if (
            not weakness_data.item_code.startswith("W")
            or not weakness_data.item_code[1:].isdigit()
        ):
            raise HTTPException(
                status_code=400, detail="Invalid item code format for weaknesses"
            )

        # Validate subvirtue IDs
        for sv_id in weakness_data.suggested_subvirtue_ids:
            try:
                subvirtue = await subvirtues.find_one({"_id": ObjectId(sv_id)})
                if not subvirtue:
                    raise HTTPException(
                        status_code=404, detail=f"Subvirtue with ID {sv_id} not found"
                    )
            except:
                raise HTTPException(
                    status_code=400, detail=f"Invalid subvirtue ID format: {sv_id}"
                )

        update_data = weakness_data.dict()

        await weaknesses.update_one(
            {"_id": ObjectId(weakness_id)}, {"$set": update_data}
        )

        updated_weakness = await weaknesses.find_one({"_id": ObjectId(weakness_id)})
        if not updated_weakness:
            raise HTTPException(status_code=404, detail="Weakness not found")

        updated_weakness["_id"] = str(updated_weakness["_id"])
        return updated_weakness
    except Exception as e:
        if "Invalid subvirtue ID format" in str(e) or "not found" in str(e):
            raise e
        raise HTTPException(status_code=400, detail="Invalid ID format")


@router.delete("/weaknesses/{weakness_id}")
async def delete_weakness(weakness_id: str):
    try:
        result = await weaknesses.delete_one({"_id": ObjectId(weakness_id)})
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Weakness not found")
        return {"status": "deleted"}
    except:
        raise HTTPException(status_code=400, detail="Invalid ID format")
