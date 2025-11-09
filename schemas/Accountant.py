from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

class AccountantCreate(BaseModel):
    """
    Модель для регистрации нового бухгалтера (входящие данные от клиента).
    """
    login: str
    password: str
    full_name: str

class AccountantLogin(BaseModel):
    """
    Модель для авторизации бухгалтера (входящие учетные данные от клиента).
    """
    login: str
    password: str
    

class AccountantPublic(BaseModel):
    """
    Модель для публичного представления данных бухгалтера (исходящие данные к клиенту).
    НЕ включает хешированный пароль.
    """
    id: int 
    login: str
    model_config = ConfigDict(from_attributes=True)

#class Config:
#   ConfigDict(from_attributes=True)