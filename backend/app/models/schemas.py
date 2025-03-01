from typing import List, Dict, Optional
from pydantic import BaseModel
from datetime import datetime


# Simple translation dictionary
class TranslationDict(BaseModel):
    en: str
    mr: str


# Main Virtue models
class MainVirtueCreate(BaseModel):
    name: TranslationDict
    description: Optional[TranslationDict] = None


# Subvirtue models
class SubvirtueCreate(BaseModel):
    name: TranslationDict
    description: Optional[TranslationDict] = None
    main_virtue_id: str


# Question models
class QuestionCreate(BaseModel):
    content: TranslationDict
    subvirtue_id: str


# Weakness models
class WeaknessCreate(BaseModel):
    name: TranslationDict
    description: Optional[TranslationDict] = None
    group: str
    suggested_subvirtue_ids: List[str]
