from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

class LabAssistantCreate(BaseModel):
    """
    Модель для регистрации нового лаборанта (входящие данные от клиента).
    """
    login: str
    password: str 
    full_name: str

class LabAssistantLogin(BaseModel):
    """
    Модель для авторизации лаборанта (входящие учетные данные от клиента).
    """
    login: str
    password: str

class LabAssistantPublic(BaseModel):
    """
    Модель для публичного представления данных лаборанта (исходящие данные к клиенту).
    НЕ включает хешированный пароль.
    """
    id: int
    login: str
    full_name: str
    last_login: Optional[datetime] = None
    services_provided: Optional[str] = None

    class Config:
        ConfigDict(from_attributes=True)