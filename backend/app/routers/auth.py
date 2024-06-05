from fastapi import APIRouter

from app.auth.models import CreateUser
from app.auth.service import register_user


router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.post("/register")
async def register_new_user(user: CreateUser):
    created = register_user(user)
    return created
