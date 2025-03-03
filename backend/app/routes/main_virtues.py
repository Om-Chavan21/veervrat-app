from fastapi import APIRouter, HTTPException, status
from bson.objectid import ObjectId
from typing import List

from app.models.schemas import MainVirtueCreate
from app.database.mongodb import main_virtues, weaknesses, subvirtues, questions

router = APIRouter()


@router.delete("/main-virtues/super-delete")
async def super_delete_main_virtues():
    try:
        await main_virtues.delete_many({})
        return {"status": "all deleted"}
    except:
        raise HTTPException(status_code=400, detail="Failed to delete")


# Main Virtues endpoints
@router.post("/main-virtues/")
async def create_main_virtue(virtue: MainVirtueCreate):
    # Validate item_code format for main virtues
    if not virtue.item_code.endswith(".0.0"):
        raise HTTPException(
            status_code=400, detail="Invalid item code format for main virtues"
        )

    # Check if item_code already exists in any collection
    if (
        await main_virtues.find_one({"item_code": virtue.item_code})
        or await weaknesses.find_one({"item_code": virtue.item_code})
        or await subvirtues.find_one({"item_code": virtue.item_code})
        or await questions.find_one({"item_code": virtue.item_code})
    ):
        raise HTTPException(status_code=400, detail="Item code already exists")

    new_virtue = virtue.dict()
    result = await main_virtues.insert_one(new_virtue)
    created_virtue = await main_virtues.find_one({"_id": result.inserted_id})
    created_virtue["_id"] = str(created_virtue["_id"])
    return created_virtue


@router.get("/main-virtues/")
async def get_all_main_virtues():
    virtues = await main_virtues.find().to_list(1000)
    for virtue in virtues:
        virtue["_id"] = str(virtue["_id"])
    return virtues


@router.get("/main-virtues/{virtue_id}")
async def get_main_virtue(virtue_id: str):
    try:
        virtue = await main_virtues.find_one({"_id": ObjectId(virtue_id)})
        if not virtue:
            raise HTTPException(status_code=404, detail="Main virtue not found")
        virtue["_id"] = str(virtue["_id"])
        return virtue
    except:
        raise HTTPException(status_code=400, detail="Invalid ID format")


@router.put("/main-virtues/{virtue_id}")
async def update_main_virtue(virtue_id: str, virtue_data: MainVirtueCreate):
    try:
        # Check if item_code already exists for another document in any collection
        if (
            await main_virtues.find_one(
                {
                    "item_code": virtue_data.item_code,
                    "_id": {"$ne": ObjectId(virtue_id)},
                }
            )
            or await weaknesses.find_one({"item_code": virtue_data.item_code})
            or await subvirtues.find_one({"item_code": virtue_data.item_code})
            or await questions.find_one({"item_code": virtue_data.item_code})
        ):
            raise HTTPException(status_code=400, detail="Item code already exists")

        # Validate item_code format for main virtues
        if not virtue_data.item_code.endswith(".0.0"):
            raise HTTPException(
                status_code=400, detail="Invalid item code format for main virtues"
            )

        update_data = virtue_data.dict()

        await main_virtues.update_one(
            {"_id": ObjectId(virtue_id)}, {"$set": update_data}
        )

        updated_virtue = await main_virtues.find_one({"_id": ObjectId(virtue_id)})
        if not updated_virtue:
            raise HTTPException(status_code=404, detail="Main virtue not found")
        updated_virtue["_id"] = str(updated_virtue["_id"])
        return updated_virtue
    except:
        raise HTTPException(status_code=400, detail="Invalid ID format")


@router.delete("/main-virtues/{virtue_id}")
async def delete_main_virtue(virtue_id: str):
    try:
        # Check if any subvirtue references this main virtue
        if await subvirtues.find_one({"main_virtue_id": virtue_id}):
            raise HTTPException(
                status_code=400,
                detail="Cannot delete main virtue with referenced subvirtues",
            )

        result = await main_virtues.delete_one({"_id": ObjectId(virtue_id)})
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Main virtue not found")
        return {"status": "deleted"}
    except:
        raise HTTPException(status_code=400, detail="Invalid ID format")
