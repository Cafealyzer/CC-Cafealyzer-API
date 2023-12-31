from typing import Optional, Any
from beanie import Document, Indexed, PydanticObjectId
from pydantic import BaseModel, EmailStr, Field
from fastapi.security import HTTPBasicCredentials

class User(Document):
  username: str = Field(...)
  email: EmailStr
  password: str = Field(...)
  
  class Config:
    json_schema_extra = {
      "example": {
        "username": "johndoe",
        "email": "johndoe@gmail.com",
        "password": "secret"
      }
    }
  
  class Settings:
    name = "user"

class UpdateUser(BaseModel):
  username: Optional[str]
  email: Optional[EmailStr]
  password: Optional[str]

  class Config:
    json_schema_extra = {
      "example": {
        "username": "johndoee",
        "email": "johndoe@gmail.com",
        "password": "secret"
      }
    }

class UserLogin(HTTPBasicCredentials):
  class Config:
    json_schema_extra = {
      "example": {
        "username": "johndoe", 
        "password": "secret"
      }
    }

class UserData(BaseModel):
  id: PydanticObjectId
  username: str = Field(...)
  email: EmailStr
  
  class Config:
    json_schema_extra = {
      "example": {
        "_id": "5f8a5e3b9f3c2e4c9e3a7b9f",
        "username": "johndoe",
        "email": "johndoe@gmail.com",
      }
    }