from datetime import datetime
from enum import Enum, IntEnum
from pydantic import BaseModel, Field, EmailStr, field_validator, Json, validator
from typing import Any, Dict, Optional
from models.schemas.project import ProjectDBValidator


class ChartEnum(str, Enum):
    two_d = "2d"
    three_d = "3d"
    surface = "surface"
    


class ChartBaseValidator(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=2, strict=True)
    type: ChartEnum
    axes: Dict[str, Any]



class ChartGetValidator(ChartBaseValidator):
    id: int
    plotData: Dict[str, Any]

class ChartsGetValidator(BaseModel):
    charts: list[ChartBaseValidator]
    projsData: list[ProjectDBValidator]



class ChartPostValidator(ChartBaseValidator):
    project_id: int