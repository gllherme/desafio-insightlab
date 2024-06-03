from fastapi import APIRouter

from app.models.country_profile import CountryProfile
from app.models.country_data import CountryData
from app.models.country_code import CountryCode

from app.services.country_profile import get_country_profile
from app.services.country_data import get_country_data_by_indicator
from app.services.country_codes import get_all_country_codes


router = APIRouter(
    prefix="/country",
    tags=["Country"]
)


@router.get("/profile/{code}")
async def get_country_profile_by_country_code(code: str) -> CountryProfile:
    return get_country_profile(code)


@router.get("/{code}/query/{indicator_id}")
async def get_country_query(code: str, indicator_id: str) -> CountryData:
    return get_country_data_by_indicator(code, indicator_id)


@router.get("/codes")
async def get_all_codes() -> list[CountryCode]:
    return get_all_country_codes()
