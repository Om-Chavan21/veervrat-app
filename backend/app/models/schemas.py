from typing import List, Dict, Optional
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
