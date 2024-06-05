from pydantic import BaseModel


class BaseUser(BaseModel):
    username: str


class User(BaseUser):
    password: str


class UserInDb(BaseUser):
    hashed_password: str
