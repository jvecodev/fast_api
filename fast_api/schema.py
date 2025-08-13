# fast_api/schema.py
from pydantic import BaseModel, EmailStr
from typing import List

class Message(BaseModel):
    message: str

class UserSchema(BaseModel):
    name: str
    email: EmailStr

class UserPublic(UserSchema):
    id: str

class UserList(BaseModel):
    users: List[UserPublic]
