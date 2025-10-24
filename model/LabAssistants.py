from typing import Optional
from datetime import date, datetime
from sqlmodel import SQLModel, Field
from pydantic import BaseModel, EmailStr 

class LabAssistants(SQLModel, table=True):
    id: int = Field(primary_key=True)
    login: str
    full_name: str
    last_login: Optional[datetime] = None
    services_provided: Optional[str] = None
    hashed_password: str


class LabAssistantCreate(BaseModel):
    login: str
    password: str 
    full_name: str

class LabAssistantLogin(BaseModel):
    login: str
    password: str 


class LabAssistantPublic(BaseModel):
    id: int
    login: str
    full_name: str
    last_login: Optional[datetime] = None
    services_provided: Optional[str] = None

class Config:
    # Это необходимо, чтобы Pydantic мог работать с объектами SQLModel
    # (то есть, он поймет, что это ORM-объект, а не просто словарь)
    orm_mode = True