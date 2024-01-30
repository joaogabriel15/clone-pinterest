import enum
from sqlalchemy import Column, Integer, String, Float, Enum, Boolean
from app.database import Base



class File(Base):
    __tablename__ = "file"
    
    id               = Column(Integer, primary_key=True, index=True)
    id_user          = Column(Integer, index=True)
    file_url         = Column(String, unique=True)
    file_name        = Column(String)
    file_description = Column(String)
    file_type        = Column(String)
    file_hash        = Column(String)
    file_size        = Column(Float)
    public           = Column(Boolean, default=True)