from typing import Optional
from datetime import date, datetime
from sqlmodel import SQLModel, Field

class Accountants(SQLModel, table=True):
    id: int = Field(primary_key=True)
    login_buh: str
    full_name_buh: str
    last_login_buh: Optional[datetime] = None
    billed_insurance_companies: Optional[str] = None
    hashed_password: str