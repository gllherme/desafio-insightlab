from typing import Any, Dict
from fastapi import HTTPException


class InvalidCredentialsHTTPException(HTTPException):
    def __init__(self, status_code: int, detail: Any = None, headers: Dict[str, str] | None = None) -> None:
        super().__init__(status_code, detail, headers)
