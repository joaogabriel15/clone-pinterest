from fastapi import APIRouter, status, HTTPException
from fastapi.responses import RedirectResponse
from app.utils.auth import get_password_hash, create_access_token, create_refresh_token, validate_authenticate_user
from uuid import uuid4
from typing import Dict
from pydantic import BaseModel

routes_auth = APIRouter()

class User(BaseModel):
    email: str
    password: str


@routes_auth.post("/token")
async def token(data:User) -> str:
     
    user:Dict[str, str] = {
        'email': "usuario@gmail.com",
        'password': get_password_hash("usuario")
    }

    if user is not None: 
        if validate_authenticate_user(data.password, user['password']) is False:
            raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email or Password are wrong"
        )

        return create_access_token(subject=user['email'])

    raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email or Password are wrong"
        )




@routes_auth.post("/refresh-token")
async def refresh_token(subject: str, expires_delta: int = None):
    return create_refresh_token(subject, expires_delta)
