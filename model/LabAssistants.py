from typing import Optional
from datetime import date, datetime
from sqlmodel import SQLModel, Field

class LabAssistants(SQLModel, table=True):
    id: int = Field(primary_key=True)
    login: str
    full_name: str
    last_login: Optional[datetime] = None
    services_provided: Optional[str] = None
    hashed_password: str

