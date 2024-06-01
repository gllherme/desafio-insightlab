from fastapi import FastAPI
from app.config import COUNTRY_PROFILE_BASE_URL

from app.services.country_codes import get_all_country_codes
from app.services.country_profile import get_country_profile
from app.services.indicators import get_all_indicators
from app.models.country_code import CountryCode
from app.models.country_profile import CountryProfile
from app.models.indicator import IndicatorGroup

app = FastAPI()


@app.get("/")
async def status():
    return {"Ok"}


@app.get("/country/profile/{code}", tags=["Country"])
async def get_country_profile_by_country_code(code: str) -> CountryProfile:
    return get_country_profile(code)


@app.get("/country/codes", tags=["Utils"])
async def get_country_codes() -> list[CountryCode]:
    return get_all_country_codes()


@app.get("/indicators/all", tags=["Utils"])
async def get_all_indicators_grouped() -> IndicatorGroup:
    return get_all_indicators()
