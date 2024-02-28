from typing import Annotated
from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from fastapi.responses import RedirectResponse
from app.models.UserModel import User
from app.schemas.UserSchema import UserSchema
from app.controllers.user_controller import create_user, alter_user, delete_user, get_users
from app.database import SessionLocal


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

user_routes = APIRouter(prefix='/users')
db = SessionLocal()


@user_routes.post("/search")
async def search_users(data:UserSchema, token: Annotated[str, Depends(oauth2_scheme)]):
    result = get_users(db, data)
    return result


@user_routes.post("/create")
def create_route(data:UserSchema):
    user = User(
        name=data.name,
        email=data.email,
        hashed_password=data.password,
        birth=data.birth,
        is_active=True
    )

    result =  create_user(db, user)
    return result


@user_routes.post("/alter")
def alter_route(user_data:UserSchema, token: Annotated[str, Depends(oauth2_scheme)]):

    result =  alter_user(db, user_data)
    return result

@user_routes.post("/delete")
def delete_route(id_user:str, token: Annotated[str, Depends(oauth2_scheme)]):

    result =  delete_user(db, id_user)
    return result



