from pydantic import BaseModel
from typing import Dict


class Indicator(BaseModel):
    id: int
    name: str


class IndicatorGroup(BaseModel):
    groups: Dict[str, list[Indicator]]
