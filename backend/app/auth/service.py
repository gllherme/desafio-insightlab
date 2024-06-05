from passlib.hash import bcrypt

from app.database import users_collection
from app.auth.models import CreateUser, UserInDb, BaseUser
from app.exceptions.user_already_exists_exception import UserAlreadyExistsException


def hash_password(password: str):
    return bcrypt.hash(password)


def register_user(user: CreateUser):
    user_in_db = users_collection.find_one({"username": user.username})
    if user_in_db:
        raise UserAlreadyExistsException(username=user.username)

    hashed_password = hash_password(user.password)
    user_in_db = UserInDb(username=user.username,
                          hashed_password=hashed_password)

    users_collection.insert_one(user_in_db.model_dump())

    return BaseUser(username=user.username)
