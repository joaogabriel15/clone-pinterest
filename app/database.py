from dotenv import load_dotenv
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

DB_DATABASE_TYPE = getenv("DB_DATABASE_TYPE")
DB_ANDRESS = getenv("DB_ANDRESS")
DB_PORT = getenv("DB_PORT")
DB_USER = getenv("DB_USER")
DB_PASSWORD = getenv("DB_PASSWORD")
DB_DATABASE_NAME= getenv("DB_DATABASE_NAME")

DB_URL = f'{DB_DATABASE_TYPE}://{DB_USER}:{DB_PASSWORD}@{DB_ANDRESS}:{DB_PORT or 5432}/{DB_DATABASE_NAME}'

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()