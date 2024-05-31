from fastapi import FastAPI
from app.config import COUNTRY_PROFILE_BASE_URL

from app.services.country_codes import get_all_country_codes
from app.services.country_profile import get_country_profile
from app.services.indicators import get_all_indicators
from app.models.country_code import CountryCode
from app.models.country_profile import CountryProfile

app = FastAPI()


@app.get("/")
async def status():
    return {"Ok"}


@app.get("/country/codes")
async def get_country_codes() -> list[CountryCode]:
    return get_all_country_codes()


@app.get("/country/profile/{code}")
async def get_country_profile_by_code(code: str) -> CountryProfile:
    return get_country_profile(code)


@app.get("/indicators/all")
async def get_all_indicators_grouped():
    return get_all_indicators()
