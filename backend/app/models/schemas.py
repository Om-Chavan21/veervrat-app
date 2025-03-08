from typing import List, Dict, Optional, Any
from pydantic import BaseModel
from datetime import datetime


# Simple translation dictionary
class TranslationDict(BaseModel):
    en: str
    mr: str


# Main Virtue models
class MainVirtueCreate(BaseModel):
    item_code: str
    name: TranslationDict
    # description: Optional[TranslationDict] = None


# Subvirtue models
class SubvirtueCreate(BaseModel):
    item_code: str
    name: TranslationDict
    # description: Optional[TranslationDict] = None
    main_virtue_id: str


# Question models
class QuestionCreate(BaseModel):
    item_code: str
    content: TranslationDict
    subvirtue_id: str


# Weakness models
class WeaknessCreate(BaseModel):
    item_code: str
    name: TranslationDict
    # description: Optional[TranslationDict] = None
    group: str
    suggested_subvirtue_ids: List[str]


class DalCreate(BaseModel):
    item_code: str
    name: TranslationDict
    short_name: TranslationDict
    type: TranslationDict
    email: str


from datetime import datetime


class UserCreate(BaseModel):
    name: TranslationDict
    description: TranslationDict
    dal_id: str
    whatsappNumber: str
    email: str
    password: str


class User(BaseModel):
    name: TranslationDict
    description: TranslationDict
    dal_id: str
    whatsappNumber: str
    email: str


# For questionnaire responses
class QuestionResponse(BaseModel):
    question_id: str
    answer: str  # 'Always', 'Sometimes', 'Rarely', 'Never'


class WeaknessSelection(BaseModel):
    weakness_id: str


class QuestionnaireCreate(BaseModel):
    user_id: Optional[str] = None
    group_a_weaknesses: List[WeaknessSelection]
    group_b_weaknesses: List[WeaknessSelection]
    group_c_weaknesses: List[WeaknessSelection]
    responses: List[QuestionResponse]
    created_at: Optional[datetime] = None


class QuestionnaireResponse(BaseModel):
    id: str
    user_id: str
    group_a_weaknesses: List[Any]
    group_b_weaknesses: List[Any]
    group_c_weaknesses: List[Any]
    responses: List[Any]
    created_at: datetime
