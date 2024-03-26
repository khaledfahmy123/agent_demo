from datetime import datetime
from enum import Enum, IntEnum
from typing import Dict, Any, Optional
from pydantic import BaseModel, Field, EmailStr, PrivateAttr, field_validator, Json, validator




class ProjectBaseValidator(BaseModel):
    id: Optional[int] = None
    name: str
    creator_id: Optional[int] = 1
    
    
    class Config:
        validate_assignment = True
    
    @validator('creator_id')
    def set_name(cls, creator_id):
        return creator_id or 1
    
    def __init__(self, **data):
        super().__init__(**{k: v for k, v in data.items() if k in self.__fields__})


class ProjectPostValidator(ProjectBaseValidator):
    data: list

class ProjectDBValidator(ProjectBaseValidator):
    vars: list