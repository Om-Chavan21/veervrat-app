from fastapi import APIRouter, HTTPException, status
from bson.objectid import ObjectId
from typing import List

from app.models.schemas import DalCreate
from app.database.mongodb import dals, main_virtues, weaknesses, subvirtues, questions

router = APIRouter()


@router.delete("/dals/super-delete")
async def super_delete_dals():
    try:
        await dals.delete_many({})
        return {"status": "all deleted"}
    except:
        raise HTTPException(status_code=400, detail="Failed to delete")


@router.post("/dals/")
async def create_dal(dal: DalCreate):
    # Validate item_code format for dals
    if not dal.item_code.startswith("D") or not dal.item_code[1:].isdigit():
        raise HTTPException(
            status_code=400,
            detail="Invalid item code format for dals. Should be like D001.",
        )

    # Check if item_code already exists in any collection
    if (
        await main_virtues.find_one({"item_code": dal.item_code})
        or await weaknesses.find_one({"item_code": dal.item_code})
        or await subvirtues.find_one({"item_code": dal.item_code})
        or await questions.find_one({"item_code": dal.item_code})
        or await dals.find_one({"item_code": dal.item_code})
    ):
        raise HTTPException(status_code=400, detail="Item code already exists")

    new_dal = dal.dict()
    result = await dals.insert_one(new_dal)
    created_dal = await dals.find_one({"_id": result.inserted_id})
    created_dal["_id"] = str(created_dal["_id"])
    return created_dal


@router.get("/dals/")
async def get_all_dals():
    dal_list = await dals.find().to_list(1000)
    for dal in dal_list:
        dal["_id"] = str(dal["_id"])
    return dal_list


@router.get("/dals/{dal_id}")
async def get_dal(dal_id: str):
    try:
        dal = await dals.find_one({"_id": ObjectId(dal_id)})
        if not dal:
            raise HTTPException(status_code=404, detail="Dal not found")
        dal["_id"] = str(dal["_id"])
        return dal
    except:
        raise HTTPException(status_code=400, detail="Invalid ID format")


@router.put("/dals/{dal_id}")
async def update_dal(dal_id: str, dal_data: DalCreate):
    try:
        # Check if item_code already exists for another document in any collection
        if (
            await main_virtues.find_one({"item_code": dal_data.item_code})
            or await weaknesses.find_one({"item_code": dal_data.item_code})
            or await subvirtues.find_one({"item_code": dal_data.item_code})
            or await questions.find_one({"item_code": dal_data.item_code})
            or await dals.find_one(
                {
                    "item_code": dal_data.item_code,
                    "_id": {"$ne": ObjectId(dal_id)},
                }
            )
        ):
            raise HTTPException(status_code=400, detail="Item code already exists")

        # Validate item_code format for dals
        if (
            not dal_data.item_code.startswith("D")
            or not dal_data.item_code[1:].isdigit()
        ):
            raise HTTPException(
                status_code=400,
                detail="Invalid item code format for dals. Should be like D001.",
            )

        update_data = dal_data.dict()

        await dals.update_one({"_id": ObjectId(dal_id)}, {"$set": update_data})

        updated_dal = await dals.find_one({"_id": ObjectId(dal_id)})
        if not updated_dal:
            raise HTTPException(status_code=404, detail="Dal not found")
        updated_dal["_id"] = str(updated_dal["_id"])
        return updated_dal
    except:
        raise HTTPException(status_code=400, detail="Invalid ID format")


@router.delete("/dals/{dal_id}")
async def delete_dal(dal_id: str):
    try:
        result = await dals.delete_one({"_id": ObjectId(dal_id)})
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Dal not found")
        return {"status": "deleted"}
    except:
        raise HTTPException(status_code=400, detail="Invalid ID format")
