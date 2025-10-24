from fastapi import FastAPI,HTTPException
from controller import LabAssistants_Controller
from model import LabAssistants
from typing import Optional
from datetime import date, datetime
app = FastAPI()

@app.post("/lab_assistants/register", response_model= LabAssistants)
async def register_lab_assistant(login_data:str, full_name_data: str,last_login_data:Optional[datetime] = None,services_provided_data: Optional[str] = None, password: str ="" ):
    lab_assistant = LabAssistants_Controller.add_lab(login_data, full_name_data,last_login_data,services_provided_data, password)
    if lab_assistant:
        return lab_assistant
    else:
        raise HTTPException(status_code=401)
    

@app.post("/lab_assistants/login", response_model=LabAssistants)  # Используем POST для логина
async def login_lab_assistant(login: str, password: str):  # Принимаем логин и пароль как параметры
    lab_assistant = LabAssistants_Controller.get_lab_by_login(login, password) # Получаем лаборанта из контроллера
    if lab_assistant:
        return lab_assistant  # Возвращаем данные лаборанта (Pydantic model)
    else:
        raise HTTPException(status_code=401, detail="Invalid login or password")  # Ошибка аутентификации