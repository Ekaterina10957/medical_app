from typing import Optional
from datetime import date, datetime
from sqlmodel import SQLModel, Field

class Administrator(SQLModel, table=True):
    id: int = Field(primary_key=True)
    login: str
    hashed_password: str
    phone: Optional[str] = None
    