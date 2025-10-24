from fastapi import FastAPI, HTTPException, Depends
from model.LabAssistants import LabAssistants # Твоя SQLModel
from controller.LabAssistants_Controller import LabAssistants_Controller, get_password_hash, verify_password # Твой контроллер
from db.database import get_session, init_db # Функция для получения сессии БД
from typing import Optional
from datetime import date, datetime
from sqlmodel import Session
from schemas.LabAssistant import LabAssistantCreate, LabAssistantLogin, LabAssistantPublic
app = FastAPI()


@app.on_event("startup")
def on_startup():
    init_db()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Medical Analysis API!"}

# --- Эндпоинт для регистрации лаборанта ---
@app.post("/lab_assistants/register", response_model=LabAssistantPublic, status_code=201) 
async def register_lab_assistant_api(
    lab_assistant_data: LabAssistantCreate, 
    session: Session = Depends(get_session) 
):
    # 1. Проверить, существует ли логин
    existing_lab = LabAssistants_Controller.get_lab_by_login_for_auth(session, lab_assistant_data.login)
    if existing_lab:
        raise HTTPException(status_code=400, detail="Login already registered.")
    created_lab = LabAssistants_Controller.create_lab_assistant(session, lab_assistant_data)
    return created_lab
    

@app.post("/lab_assistants/login", response_model=LabAssistants)  # Используем POST для логина
async def login_lab_assistant(login: str, password: str):  # Принимаем логин и пароль как параметры
    lab_assistant = LabAssistants_Controller.get_lab_by_login(login, password) # Получаем лаборанта из контроллера
    if lab_assistant:
        return lab_assistant  # Возвращаем данные лаборанта (Pydantic model)
    else:
        raise HTTPException(status_code=401, detail="Invalid login or password")  # Ошибка аутентификации
    

# --- Эндпоинт для авторизации лаборанта ---
@app.post("/lab_assistants/login", response_model=LabAssistantPublic) 
async def login_lab_assistant_api(
    credentials: LabAssistantLogin, 
    session: Session = Depends(get_session)
):
    # 1. Получить лаборанта по логину из БД
    lab_assistant_db = LabAssistants_Controller.get_lab_by_login_for_auth(session, credentials.login)

    # 2. Проверить существование лаборанта и верифицировать пароль
    if not lab_assistant_db or not verify_password(credentials.password, lab_assistant_db.hashed_password):
        raise HTTPException(status_code=401, detail="Incorrect login or password.")

    # 3. Если все успешно, обновить время последнего входа
    updated_lab = LabAssistants_Controller.update_lab_assistant_last_login(session, lab_assistant_db)
    
    # 4. Вернуть публичную версию лаборанта (или JWT-токен)
    return updated_lab