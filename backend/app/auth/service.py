from fastapi import Depends
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from datetime import timedelta, datetime, timezone
from typing import Annotated
from jwt.exceptions import InvalidTokenError
import jwt

from app.database import users_collection
from app.auth.models import User, UserInDb, BaseUser, Token, TokenData
from app.exceptions.user_already_exists_exception import UserAlreadyExistsException
from app.auth.exceptions import InvalidCredentialsHTTPException

# openssl rand -hex 32
SECRET_KEY = "f2365836972e5bd53a9869ad8e6e3bd5205335c4545ad944d965919d7f67d74d"
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")


def verify_password(password, hashed_password):
    return pwd_context.verify(password, hashed_password)


def hash_password(password: str):
    return pwd_context.hash(password)


def get_user(username: str):
    return users_collection.find_one({"username": username})


def authenticate_user(username, password):
    user = get_user(username)
    if not user:
        return False
    if not verify_password(password, user["hashed_password"]):
        return False

    return BaseUser(username=user["username"])


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = InvalidCredentialsHTTPException(
        status_code=401,
        detail="Credenciais Invalidas",
        headers={"WWW-Authenticate": "Bearer"}
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except InvalidTokenError:
        raise credentials_exception
    user = get_user(username=token_data.username)
    if user is None:
        raise credentials_exception

    return BaseUser(username=user["username"])


async def get_current_active_user(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(minutes=15)

    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


def register_user(user: User):
    user_in_db = get_user(user.username)
    if user_in_db:
        raise UserAlreadyExistsException(username=user.username)

    hashed_password = hash_password(user.password)
    user_in_db = UserInDb(username=user.username,
                          hashed_password=hashed_password)

    users_collection.insert_one(user_in_db.model_dump())

    return BaseUser(username=user.username)
