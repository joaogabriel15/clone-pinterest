from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
from app.database import Base


class User(Base):
    __tablename__ = "user"
    
    id              = Column(Integer, primary_key=True, index=True)
    email           = Column(String, unique=True, index=True)
    name            = Column(String)
    hashed_password = Column(String)
    birth           = Column(Date)
    is_active       = Column(Boolean, default=True)