from datetime import date
from pydantic import BaseModel

class UserSchema(BaseModel):
    id:        int  | None
    email:     str  | None
    name:      str  | None
    password:  str  | None
    birth:     date | None
    is_active: bool | None

class LoginSchema(BaseModel):
    id:        int  | None
    email:     str  | None
    password:  str  | None