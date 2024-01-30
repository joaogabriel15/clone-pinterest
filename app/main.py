from dotenv import load_dotenv
from typing import Annotated
from fastapi import FastAPI, Depends
from app.models import UserModel
from app.database import SessionLocal, engine
from app.api.auth_route import routes_auth
from app.api.user_route import user_routes
from app.api.file_route import file_routes

# Carregando valores .env para as variaveis de ambiente
load_dotenv()

UserModel.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




app = FastAPI()

app.include_router(routes_auth)
app.include_router(user_routes)
app.include_router(file_routes)