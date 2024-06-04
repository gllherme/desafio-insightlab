from fastapi import Request
from fastapi.responses import JSONResponse


class BadFilterValueException(Exception):
    def __init__(self, error_msg: str):
        self.error_msg = error_msg


async def bad_filter_exception_handler(request: Request, exc: BadFilterValueException):
    return JSONResponse(
        status_code=400,
        content={"message": f"ERRO - '{exc.error_msg}'"}
    )
