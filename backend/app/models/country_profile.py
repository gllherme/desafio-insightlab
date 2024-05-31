from pydantic import BaseModel


class CountryProfile(BaseModel):
    code: str
    name: str
    area: float  # km2
    region: str
    languages: list[str]
    currencies: list[str]
