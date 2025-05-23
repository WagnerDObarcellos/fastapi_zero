from typing import List
from pydantic import BaseModel, EmailStr

class Message(BaseModel):
    message: str

class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserPublic(BaseModel): 
    id: int
    username: str
    email: EmailStr

class UserList(BaseModel):
    users: List[UserPublic]

class UserDB(UserSchema):
    id: int
