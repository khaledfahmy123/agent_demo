from datetime import datetime
from enum import Enum, IntEnum
from typing import Dict, Any
from pydantic import BaseModel, Field, EmailStr, PrivateAttr, field_validator, Json




class ProjectDataValidator(BaseModel):
    data_path: str
    
    def __init__(self, **data):
        super().__init__(**{k: v for k, v in data.items() if k in self.__fields__})