from fastapi import Request
from fastapi.responses import JSONResponse


class UserAlreadyExistsException(Exception):
    def __init__(self, username: str):
        self.username = username


async def user_already_exists_exception_handler(request: Request, exc: UserAlreadyExistsException):
    return JSONResponse(
        status_code=400,
        content={"message": f"O usuário '{exc.username}' já existe"}
    )
