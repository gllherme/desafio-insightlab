from pydantic import BaseModel


class Indicator(BaseModel):
    id: int
    name: str


class IndicatorGroup(BaseModel):
    group: str
    indicators: list[Indicator]
