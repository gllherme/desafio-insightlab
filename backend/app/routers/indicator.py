from fastapi import APIRouter

from app.models.indicator import IndicatorGroup
from app.services.indicators import get_all_indicators


router = APIRouter(
    prefix="/indicator",
    tags=["Indicator"]
)


@router.get("/indicators/all")
async def get_all_indicators_grouped() -> list[IndicatorGroup]:
    return get_all_indicators()
