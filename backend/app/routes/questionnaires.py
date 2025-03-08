# app/routes/questionnaires.py

from fastapi import APIRouter, HTTPException, status, Depends
from typing import List, Optional
from bson.objectid import ObjectId
import datetime
import random

from app.routes.users import get_current_user
from app.models.schemas import QuestionnaireCreate, QuestionResponse, WeaknessSelection
from app.database.mongodb import questionnaires, weaknesses, questions, subvirtues

router = APIRouter()


@router.post("/questionnaires/")
async def create_questionnaire(
    questionnaire_data: QuestionnaireCreate,
    current_user: dict = Depends(get_current_user),
):
    try:
        # Validate that we have exactly 2 weaknesses per group
        if (
            len(questionnaire_data.group_a_weaknesses) != 2
            or len(questionnaire_data.group_b_weaknesses) != 2
            or len(questionnaire_data.group_c_weaknesses) != 2
        ):
            raise HTTPException(
                status_code=400,
                detail="Must select exactly 2 weaknesses from each group",
            )

        # Set user_id from authenticated user
        questionnaire_data.user_id = str(current_user["_id"])

        # Set creation timestamp
        questionnaire_data.created_at = datetime.datetime.utcnow()

        # Save questionnaire
        result = await questionnaires.insert_one(questionnaire_data.dict())
        created_questionnaire = await questionnaires.find_one(
            {"_id": result.inserted_id}
        )

        # Convert _id to string
        created_questionnaire["_id"] = str(created_questionnaire["_id"])

        print(questionnaire_data)
        return created_questionnaire
    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))


@router.get("/questionnaires/me")
async def get_user_questionnaires(current_user: dict = Depends(get_current_user)):
    user_id = str(current_user["_id"])

    user_questionnaires = (
        await questionnaires.find({"user_id": user_id})
        .sort("created_at", -1)
        .to_list(1000)
    )

    # Process each questionnaire to include full weakness and question details
    for questionnaire in user_questionnaires:
        questionnaire["_id"] = str(questionnaire["_id"])

        # Populate weakness details for group A
        for i, weakness in enumerate(questionnaire["group_a_weaknesses"]):
            try:
                weakness_id = weakness["weakness_id"]
                if ObjectId.is_valid(weakness_id):
                    weakness_data = await weaknesses.find_one(
                        {"_id": ObjectId(weakness_id)}
                    )
                    if weakness_data:
                        weakness_data["_id"] = str(weakness_data["_id"])
                        questionnaire["group_a_weaknesses"][i] = weakness_data
            except Exception as e:
                print(f"Error processing group A weakness: {e}")

        # Populate weakness details for group B
        for i, weakness in enumerate(questionnaire["group_b_weaknesses"]):
            try:
                weakness_id = weakness["weakness_id"]
                if ObjectId.is_valid(weakness_id):
                    weakness_data = await weaknesses.find_one(
                        {"_id": ObjectId(weakness_id)}
                    )
                    if weakness_data:
                        weakness_data["_id"] = str(weakness_data["_id"])
                        questionnaire["group_b_weaknesses"][i] = weakness_data
            except Exception as e:
                print(f"Error processing group B weakness: {e}")

        # Populate weakness details for group C
        for i, weakness in enumerate(questionnaire["group_c_weaknesses"]):
            try:
                weakness_id = weakness["weakness_id"]
                if ObjectId.is_valid(weakness_id):
                    weakness_data = await weaknesses.find_one(
                        {"_id": ObjectId(weakness_id)}
                    )
                    if weakness_data:
                        weakness_data["_id"] = str(weakness_data["_id"])
                        questionnaire["group_c_weaknesses"][i] = weakness_data
            except Exception as e:
                print(f"Error processing group C weakness: {e}")

        # Populate question details
        for i, response in enumerate(questionnaire["responses"]):
            try:
                question_id = response["question_id"]
                if ObjectId.is_valid(question_id):
                    question_data = await questions.find_one(
                        {"_id": ObjectId(question_id)}
                    )
                    if question_data:
                        question_data["_id"] = str(question_data["_id"])
                        questionnaire["responses"][i]["question"] = question_data
            except Exception as e:
                print(f"Error processing question: {e}")

    return user_questionnaires


@router.get("/questionnaires/{questionnaire_id}")
async def get_questionnaire(
    questionnaire_id: str, current_user: dict = Depends(get_current_user)
):
    try:
        questionnaire = await questionnaires.find_one(
            {"_id": ObjectId(questionnaire_id)}
        )

        if not questionnaire:
            raise HTTPException(status_code=404, detail="Questionnaire not found")

        # Check if this questionnaire belongs to the current user
        if questionnaire["user_id"] != str(current_user["_id"]):
            raise HTTPException(
                status_code=403, detail="Not authorized to access this questionnaire"
            )

        questionnaire["_id"] = str(questionnaire["_id"])

        # Populate weakness details for group A
        for i, weakness in enumerate(questionnaire["group_a_weaknesses"]):
            weakness_id = weakness["weakness_id"]
            weakness_data = await weaknesses.find_one({"_id": ObjectId(weakness_id)})
            if weakness_data:
                weakness_data["_id"] = str(weakness_data["_id"])
                questionnaire["group_a_weaknesses"][i] = weakness_data

        # Populate weakness details for group B
        for i, weakness in enumerate(questionnaire["group_b_weaknesses"]):
            weakness_id = weakness["weakness_id"]
            weakness_data = await weaknesses.find_one({"_id": ObjectId(weakness_id)})
            if weakness_data:
                weakness_data["_id"] = str(weakness_data["_id"])
                questionnaire["group_b_weaknesses"][i] = weakness_data

        # Populate weakness details for group C
        for i, weakness in enumerate(questionnaire["group_c_weaknesses"]):
            weakness_id = weakness["weakness_id"]
            weakness_data = await weaknesses.find_one({"_id": ObjectId(weakness_id)})
            if weakness_data:
                weakness_data["_id"] = str(weakness_data["_id"])
                questionnaire["group_c_weaknesses"][i] = weakness_data

        # Populate question details
        for i, response in enumerate(questionnaire["responses"]):
            question_id = response["question_id"]
            question_data = await questions.find_one({"_id": ObjectId(question_id)})
            if question_data:
                question_data["_id"] = str(question_data["_id"])
                questionnaire["responses"][i]["question"] = question_data

        return questionnaire
    except:
        raise HTTPException(status_code=400, detail="Invalid ID format")


@router.delete("/questionnaires/{questionnaire_id}")
async def delete_questionnaire(
    questionnaire_id: str, current_user: dict = Depends(get_current_user)
):
    try:
        # Check if the questionnaire exists and belongs to the current user
        questionnaire = await questionnaires.find_one(
            {"_id": ObjectId(questionnaire_id)}
        )

        if not questionnaire:
            raise HTTPException(status_code=404, detail="Questionnaire not found")

        if questionnaire["user_id"] != str(current_user["_id"]):
            raise HTTPException(
                status_code=403, detail="Not authorized to delete this questionnaire"
            )

        # Delete the questionnaire
        result = await questionnaires.delete_one({"_id": ObjectId(questionnaire_id)})

        return {"status": "deleted"}
    except:
        raise HTTPException(status_code=400, detail="Invalid ID format")


# Get random set of questions based on selected weaknesses
@router.post("/questionnaires/get-random-questions")
async def get_random_questions(
    group_a_weaknesses: List[WeaknessSelection],
    group_b_weaknesses: List[WeaknessSelection],
    group_c_weaknesses: List[WeaknessSelection],
    current_user: dict = Depends(get_current_user),
):
    # Validate that we have exactly 2 weaknesses per group
    if (
        len(group_a_weaknesses) != 2
        or len(group_b_weaknesses) != 2
        or len(group_c_weaknesses) != 2
    ):
        raise HTTPException(
            status_code=400, detail="Must select exactly 2 weaknesses from each group"
        )

    # Get all selected weakness IDs
    weakness_ids = [
        *[w.weakness_id for w in group_a_weaknesses],
        *[w.weakness_id for w in group_b_weaknesses],
        *[w.weakness_id for w in group_c_weaknesses],
    ]

    # Get all subvirtue IDs related to selected weaknesses
    subvirtue_ids = set()
    for weakness_id in weakness_ids:
        try:
            weakness = await weaknesses.find_one({"_id": ObjectId(weakness_id)})
            if weakness and "suggested_subvirtue_ids" in weakness:
                subvirtue_ids.update(weakness["suggested_subvirtue_ids"])
        except:
            pass

    # Get all questions for these subvirtues
    all_questions = []
    for subvirtue_id in subvirtue_ids:
        try:
            subvirtue_questions = await questions.find(
                {"subvirtue_id": subvirtue_id}
            ).to_list(1000)
            all_questions.extend(subvirtue_questions)
        except:
            pass

    # Convert ObjectIds to strings for all questions
    for question in all_questions:
        question["_id"] = str(question["_id"])

    # If there are more than 25 questions, randomly select 25
    if len(all_questions) > 25:
        selected_questions = random.sample(all_questions, 25)
    else:
        selected_questions = all_questions

    return {"questions": selected_questions}


@router.delete("/questionnaires/super-delete")
async def super_delete_questionnaires():
    try:
        await questionnaires.delete_many({})
        return {"status": "all deleted"}
    except:
        raise HTTPException(status_code=400, detail="Failed to delete")
