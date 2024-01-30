from os import getenv
from datetime import datetime, timedelta
from typing import  Any
from jose import jwt
from passlib.context import CryptContext

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str)-> str:
    """ Transform password string to password hash

    @params password: A plain password string
    @return : A password hashed

    Basic usage:

    .. highlight:: python
    .. code-block:: python
        get_password_hash("123456")
        return $2y$10$bmm3N5stnTit5ou5Os4mUuYNtO7z2W/2ILJtHbnagEfcN4wctbPCq
    """
    return password_context.hash(password)


def validate_authenticate_user(password: str, hashed_password: str)-> bool:

    return password_context.verify(password, hashed_password)


def create_access_token(subject: str | Any, expires_delta: int = None ) -> str:
    """ Create Token """

    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes = getenv('ACCESS_TOKEN_EXPIRE_MINUTES'))

    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, getenv('JWT_SECRET_KEY'), getenv('ALGORITHM'))

    return encoded_jwt


def create_refresh_token(subject: str | Any, expires_delta: int = None) -> str:
    """ Refresh token """

    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow + timedelta(minutes = getenv('REFRESH_TOKEN_EXPIRE_MINUTES'))
    
    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, getenv('JWT_REFRESH_SECRET_KEY'), getenv('ALGORITHM'))

    return encoded_jwt