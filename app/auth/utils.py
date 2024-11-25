from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta
from auth.schemas import UserCreate, Token, UserLogin
from typing import Optional
from conf.configuration import get_settings
from fastapi import HTTPException, status

settings = get_settings()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

users = {}
users[settings.DUMMY_USERNAME] = settings.DUMMY_PASSWORD

def create_user(user: UserCreate):
    users[user.email.lower()] = user.password

def authenticate_user(user: UserLogin) -> Optional[UserLogin]:
    if user.username.lower() in users and users[user.username.lower()] == user.password:
        return user

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire.timestamp()})
    return jwt.encode(to_encode, settings.SECRET_KEY)


def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, options={"verify_exp": False})
        if "exp" in payload:
            expire = datetime.utcfromtimestamp(payload["exp"])
            if expire > datetime.utcnow():
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Token has expired",
                    headers={"WWW-Authenticate": "Bearer"},
                )

        return payload

    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )

