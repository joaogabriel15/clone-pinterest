from fastapi import APIRouter, status, HTTPException
from fastapi.responses import RedirectResponse
from app.controllers.user_controller import get_user
from app.schemas.UserSchema import LoginSchema
from app.database import SessionLocal
from app.utils.auth import get_password_hash, create_access_token, create_refresh_token, validate_authenticate_user
from uuid import uuid4
from typing import Dict
from pydantic import BaseModel

routes_auth = APIRouter()
db = SessionLocal()

@routes_auth.post("/token")
async def token(data:LoginSchema) -> str:
    # Busca o usuario.
    user = get_user(db, data) 
    # Valida se as hash de senha são iguais.
    if user is not None: 
        if validate_authenticate_user(data.password, user.hashed_password) is True:
            return create_access_token(subject=user.id, data={"name":user.name, "email":user.email} )

    raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Email or Password are wrong"
        )


@routes_auth.post("/refresh-token")
async def refresh_token(subject: str, expires_delta: int = None):
    return create_refresh_token(subject, expires_delta)
