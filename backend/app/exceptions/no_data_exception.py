from fastapi import Request
from fastapi.responses import JSONResponse


class NoDataException(Exception):
    def __init__(self, indicator_name: str):
        self.indicator_name = indicator_name


async def no_data_exception_handler(request: Request, exc: NoDataException):
    return JSONResponse(
        status_code=200,
        content={"message": f"Não há dados para o indicador '{exc.indicator_name}'"}
    )
