from fastapi import APIRouter, Path, Query, Depends
from typing import Annotated

from app.models.country_profile import CountryProfile
from app.models.country_data import CountryData
from app.models.country_code import CountryCode

from app.services.country_profile import get_country_profile
from app.services.country_data import get_country_data_by_indicator
from app.services.country_codes import get_all_country_codes

from app.exceptions.bad_filter_value_exception import BadFilterValueException

from app.auth.service import oauth2_scheme

router = APIRouter(
    prefix="/country",
    tags=["Country"],
)

code_param = Annotated[str, Path(examples=["BR"], min_length=2, max_length=2)]
indicator_param = Annotated[str, Path(
    examples=["77849"], min_length=5, max_length=5)]
year_param = Annotated[int | None, Query(examples=[2008])]


@router.get("/profile/{code}", response_model=CountryProfile)
async def get_country_profile_by_country_code(code: code_param, token: str = Depends(oauth2_scheme)):
    return get_country_profile(code)


@router.get("/{code}/query/{indicator_id}", response_model=CountryData)
async def get_country_query(code: code_param,
                            indicator_id: indicator_param,
                            start_year: year_param = None,
                            end_year: year_param = None, 
                            token: str = Depends(oauth2_scheme)
                            ):

    if (start_year and end_year) and start_year > end_year:
        raise BadFilterValueException(
            error_msg="start_year deve ser menor ou igual a end_year"
        )

    return get_country_data_by_indicator(code, indicator_id, start_year, end_year)


@router.get("/codes", response_model=list[CountryCode])
async def get_all_codes(token: str = Depends(oauth2_scheme)):
    return get_all_country_codes()
