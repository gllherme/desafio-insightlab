from pydantic import BaseModel


class BaseUser(BaseModel):
    username: str


class User(BaseUser):
    password: str


class UserInDb(BaseUser):
    hashed_password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
