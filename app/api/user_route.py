from fastapi import APIRouter, status, HTTPException
from fastapi.responses import RedirectResponse
from app.models.UserModel import User
from app.schemas.UserSchema import UserSchema
from app.controllers.user_controller import create_user, alter_user, delete_user, get_user, get_users
from app.database import SessionLocal


user_routes = APIRouter(prefix='/users')
db = SessionLocal()


@user_routes.post("/")
def gets_route():

    result =  get_users(db)
    return result


@user_routes.post("/user")
def get_route(id_user: str):

    result =  get_user(db, id_user)
    return result


@user_routes.post("/create")
def create_route(user_data:UserSchema):
    user = User(
        name=user_data.name,
        email=user_data.email,
        hashed_password=user_data.password,
        is_active=True
    )

    result =  create_user(db, user)
    return result


@user_routes.post("/alter")
def alter_route(user_data:UserSchema):

    result =  alter_user(db, user_data)
    return result

@user_routes.post("/delete")
def delete_route(id_user:str):

    result =  delete_user(db, id_user)
    return result



