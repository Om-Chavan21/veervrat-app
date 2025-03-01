from fastapi import APIRouter, HTTPException, status, Query
from bson.objectid import ObjectId
from typing import List, Optional

from app.models.schemas import WeaknessCreate  # Updated import
from app.database.mongodb import weaknesses, subvirtues

router = APIRouter()


@router.post("/weaknesses/")
async def create_weakness(weakness: WeaknessCreate):
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
