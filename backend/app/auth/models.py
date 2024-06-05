from pydantic import BaseModel


class BaseUser(BaseModel):
    username: str


class CreateUser(BaseUser):
    password: str


class UserInDb(BaseUser):
    hashed_password: str
