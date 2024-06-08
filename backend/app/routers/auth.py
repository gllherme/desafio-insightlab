from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated

from app.auth.models import User, Token, BaseUser
from app.auth.service import register_user, authenticate_user, create_access_token, get_current_active_user
from app.auth.exceptions import InvalidCredentialsHTTPException


router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.get("/me")
async def read_current_user(current_user: Annotated[User, Depends(get_current_active_user)]):
    return current_user


@router.post("/token")
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise InvalidCredentialsHTTPException(
        status_code=401,
        detail="Credenciais Invalidas",
        headers={"WWW-Authenticate": "Bearer"}
    )
    access_token = create_access_token(data={"sub": user.username})
    return Token(access_token=access_token, token_type="bearer")


@router.post("/register")
async def register_new_user(user: User):
    created = register_user(user)
    return created
