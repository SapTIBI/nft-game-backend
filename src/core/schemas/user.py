from pydantic import BaseModel
from datetime import datetime

class UserSchema(BaseModel):
    id: int
    username: str
    tgToken: str
    balance: int
    role: str
    refScore: int
    email: str
    created_at:datetime

class UserCreateSchema(BaseModel):
    username: str
    tgToken: str
    email: str

class UserUpdateSchema(BaseModel):
    username: str
    balance: int
    role: str
    refScore: int
    email: str