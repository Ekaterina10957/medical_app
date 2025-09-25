from typing import Optional
from datetime import date, datetime
from sqlmodel import SQLModel, Field, Relationship

class Patient(SQLModel, table=True):
    id: int = Field(primary_key=True)
    login: str
    full_name: str
    birthdate: date  
    passport_series: str
    passport_number: str
    phone: str
    email: str
    insurance_number: str
    insurance_type: str
    insurance_company_id: int
    password: str