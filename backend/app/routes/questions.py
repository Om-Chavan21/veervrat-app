from fastapi import APIRouter, HTTPException, status
from bson.objectid import ObjectId
from typing import List, Optional

from app.models.schemas import QuestionCreate
from app.database.mongodb import questions, subvirtues, main_virtues, weaknesses

router = APIRouter()


@router.delete("/questions/super-delete")
async def super_delete_questions():
    try:
        await questions.delete_many({})
        return {"status": "all deleted"}
    except:
        raise HTTPException(status_code=400, detail="Failed to delete")


# Modified create_question function
@router.post("/questions/")
async def create_question(question: QuestionCreate):
    # Validate item_code format for questions
    parts = question.item_code.split(".")
    if len(parts) != 4 or not all(part.isdigit() for part in parts):
        raise HTTPException(
            status_code=400, detail="Invalid item code format for questions"
        )

    # Check if item_code already exists in any collection
    if (
        await main_virtues.find_one({"item_code": question.item_code})
        or await weaknesses.find_one({"item_code": question.item_code})
        or await subvirtues.find_one({"item_code": question.item_code})
        or await questions.find_one({"item_code": question.item_code})
    ):
        raise HTTPException(status_code=400, detail="Item code already exists")

    try:
        # Check if subvirtue exists
        subvirtue = await subvirtues.find_one({"_id": ObjectId(question.subvirtue_id)})
        if not subvirtue:
            raise HTTPException(status_code=404, detail="Subvirtue not found")

        # Ensure subvirtue's item_code matches the question's first two parts
        subvirtue_parts = subvirtue["item_code"].split(".")
        if parts[0] != subvirtue_parts[0] or parts[1] != subvirtue_parts[1]:
            raise HTTPException(
                status_code=400, detail="Invalid item code for question"
            )

        new_question = question.dict()

        result = await questions.insert_one(new_question)
        created_question = await questions.find_one({"_id": result.inserted_id})
        created_question["_id"] = str(created_question["_id"])
        return created_question
    except Exception as e:
        if "Subvirtue not found" in str(e):
            raise e
        raise HTTPException(status_code=400, detail="Invalid subvirtue ID format")


@router.put("/questions/{question_id}")
async def update_question(question_id: str, question_data: QuestionCreate):
    try:
        # Check if item_code already exists for another document in any collection
        if (
            await main_virtues.find_one({"item_code": question_data.item_code})
            or await weaknesses.find_one({"item_code": question_data.item_code})
            or await subvirtues.find_one({"item_code": question_data.item_code})
            or await questions.find_one(
                {
                    "item_code": question_data.item_code,
                    "_id": {"$ne": ObjectId(question_id)},
                }
            )
        ):
            raise HTTPException(status_code=400, detail="Item code already exists")

        # Validate item_code format for questions
        parts = question_data.item_code.split(".")
        if len(parts) != 4 or not all(part.isdigit() for part in parts):
            raise HTTPException(
                status_code=400, detail="Invalid item code format for questions"
            )

        # Check if subvirtue exists
        try:
            subvirtue = await subvirtues.find_one(
                {"_id": ObjectId(question_data.subvirtue_id)}
            )
            if not subvirtue:
                raise HTTPException(status_code=404, detail="Subvirtue not found")
        except:
            raise HTTPException(status_code=400, detail="Invalid subvirtue ID format")

        # Ensure subvirtue's item_code matches the question's first two parts
        subvirtue_parts = subvirtue["item_code"].split(".")
        if parts[0] != subvirtue_parts[0] or parts[1] != subvirtue_parts[1]:
            raise HTTPException(
                status_code=400, detail="Invalid item code for question"
            )

        update_data = question_data.dict()

        await questions.update_one(
            {"_id": ObjectId(question_id)}, {"$set": update_data}
        )

        updated_question = await questions.find_one({"_id": ObjectId(question_id)})
        if not updated_question:
            raise HTTPException(status_code=404, detail="Question not found")

        updated_question["_id"] = str(updated_question["_id"])
        return updated_question
    except Exception as e:
        if "Invalid subvirtue ID format" in str(e) or "Subvirtue not found" in str(e):
            raise e
        raise HTTPException(status_code=400, detail="Invalid ID format")


@router.get("/questions/")
async def get_all_questions(subvirtue_id: Optional[str] = None):
    query = {}
    if subvirtue_id:
        try:
            # Check if subvirtue exists
            subvirtue = await subvirtues.find_one({"_id": ObjectId(subvirtue_id)})
            if not subvirtue:
                raise HTTPException(status_code=404, detail="Subvirtue not found")

            query["subvirtue_id"] = subvirtue_id
        except:
            raise HTTPException(status_code=400, detail="Invalid subvirtue ID format")

    question_list = await questions.find(query).to_list(1000)

    # Convert ObjectIds and add subvirtue information
    for question in question_list:
        question["_id"] = str(question["_id"])
        try:
            subvirtue = await subvirtues.find_one(
                {"_id": ObjectId(question["subvirtue_id"])}
            )
            if subvirtue:
                subvirtue["_id"] = str(subvirtue["_id"])
                question["subvirtue"] = subvirtue
        except:
            question["subvirtue"] = None

    return question_list


@router.get("/questions/{question_id}")
async def get_question(question_id: str):
    try:
        question = await questions.find_one({"_id": ObjectId(question_id)})
        if not question:
            raise HTTPException(status_code=404, detail="Question not found")

        question["_id"] = str(question["_id"])

        # Get subvirtue data
        try:
            subvirtue = await subvirtues.find_one(
                {"_id": ObjectId(question["subvirtue_id"])}
            )
            if subvirtue:
                subvirtue["_id"] = str(subvirtue["_id"])
                question["subvirtue"] = subvirtue
        except:
            question["subvirtue"] = None

        return question
    except:
        raise HTTPException(status_code=400, detail="Invalid ID format")


@router.put("/questions/{question_id}")
async def update_question(question_id: str, question_data: QuestionCreate):
    try:
        # Check if item_code already exists for another document in any collection
        if (
            await main_virtues.find_one({"item_code": question_data.item_code})
            or await weaknesses.find_one({"item_code": question_data.item_code})
            or await subvirtues.find_one({"item_code": question_data.item_code})
            or await questions.find_one(
                {
                    "item_code": question_data.item_code,
                    "_id": {"$ne": ObjectId(question_id)},
                }
            )
        ):
            raise HTTPException(status_code=400, detail="Item code already exists")

        # Validate item_code format for questions
        parts = question_data.item_code.split(".")
        if len(parts) != 3 or not all(part.isdigit() for part in parts):
            raise HTTPException(
                status_code=400, detail="Invalid item code format for questions"
            )

        # Check if subvirtue exists
        try:
            subvirtue = await subvirtues.find_one(
                {"_id": ObjectId(question_data.subvirtue_id)}
            )
            if not subvirtue:
                raise HTTPException(status_code=404, detail="Subvirtue not found")
        except:
            raise HTTPException(status_code=400, detail="Invalid subvirtue ID format")

        # Ensure subvirtue's item_code matches the question's first two parts
        subvirtue_parts = subvirtue["item_code"].split(".")
        if parts[0] != subvirtue_parts[0] or parts[1] != subvirtue_parts[1]:
            raise HTTPException(
                status_code=400, detail="Invalid item code for question"
            )

        update_data = question_data.dict()

        await questions.update_one(
            {"_id": ObjectId(question_id)}, {"$set": update_data}
        )

        updated_question = await questions.find_one({"_id": ObjectId(question_id)})
        if not updated_question:
            raise HTTPException(status_code=404, detail="Question not found")

        updated_question["_id"] = str(updated_question["_id"])
        return updated_question
    except Exception as e:
        if "Invalid subvirtue ID format" in str(e) or "Subvirtue not found" in str(e):
            raise e
        raise HTTPException(status_code=400, detail="Invalid ID format")


@router.delete("/questions/{question_id}")
async def delete_question(question_id: str):
    try:
        result = await questions.delete_one({"_id": ObjectId(question_id)})
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Question not found")
        return {"status": "deleted"}
    except:
        raise HTTPException(status_code=400, detail="Invalid ID format")


@router.get("/subvirtues/{subvirtue_id}/questions")
async def get_questions_by_subvirtue(subvirtue_id: str):
    try:
        # Check if subvirtue exists
        subvirtue = await subvirtues.find_one({"_id": ObjectId(subvirtue_id)})
        if not subvirtue:
            raise HTTPException(status_code=404, detail="Subvirtue not found")

        question_list = await questions.find({"subvirtue_id": subvirtue_id}).to_list(
            1000
        )

        # Convert ObjectIds to strings
        for question in question_list:
            question["_id"] = str(question["_id"])

        return question_list
    except:
        raise HTTPException
