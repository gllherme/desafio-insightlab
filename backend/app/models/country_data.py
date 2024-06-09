from pydantic import BaseModel
from typing import Dict


class DataEntry(BaseModel):
    year: str
    value: int | float


class CountryData(BaseModel):
    indicator_id: int
    indicator_name: str
    values: list[DataEntry]
