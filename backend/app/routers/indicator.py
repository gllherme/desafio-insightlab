from fastapi import APIRouter, Depends

from app.models.indicator import IndicatorGroup
from app.services.indicators import get_all_indicators

from app.auth.service import oauth2_scheme


router = APIRouter(
    prefix="/indicator",
    tags=["Indicator"]
)


@router.get("/all")
async def get_all_indicators_grouped(token: str = Depends(oauth2_scheme)) -> list[IndicatorGroup]:
    return get_all_indicators()
