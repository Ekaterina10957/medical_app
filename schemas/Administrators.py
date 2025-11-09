from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

class AdministratorsCreate(BaseModel):
    """
    Модель для регистрации нового администратора (входящие данные от клиента).
    """
    login: str
    password: str
    phone: Optional[str] = None

class AdministratorsLogin(BaseModel):
    """
    Модель для авторизации администратора (входящие учетные данные от клиента).
    """
    login: str
    password: str
    

class AdministratorsPublic(BaseModel):
    """
    Модель для публичного представления данных администратора (исходящие данные к клиенту).
    НЕ включает хешированный пароль.
    """
    id: int 
    login: str
    phone: Optional[str] = None

class Config:
    ConfigDict(from_attributes=True)