from fastapi import FastAPI, HTTPException, Depends
from sqlmodel import Session # Убедись, что это 'from sqlmodel import Session'
from model.LabAssistants import LabAssistants # Предполагаем, что файл называется lab_assistants.py в папке models
from controller.LabAssistants_Controller import LabAssistants_Controller, get_password_hash, verify_password
from db.database import get_session, init_db
from schemas.LabAssistant import LabAssistantCreate, LabAssistantLogin, LabAssistantPublic # Предполагаем, что файл называется lab_assistant.py в папке schemas
from datetime import datetime

app = FastAPI()

# --- Хук для инициализации БД при старте приложения ---
@app.on_event("startup")
def on_startup():
    init_db()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Medical Analysis API!"}

# --- Эндпоинт для регистрации лаборанта ---
@app.post("/lab_assistants/register", response_model=LabAssistantPublic, status_code=201)
async def register_lab_assistant_api(
    lab_assistant_data: LabAssistantCreate, # Входящие данные - Pydantic модель
    session: Session = Depends(get_session) # Зависимость для получения сессии БД
):
    # 1. Проверить, существует ли лаборант с таким логином
    existing_lab = LabAssistants_Controller.get_lab_by_login_for_auth(session, lab_assistant_data.login)
    if existing_lab:
        raise HTTPException(status_code=400, detail="Login already registered.")
    # 2. Создать лаборанта через контроллер (который сам хеширует пароль)
    created_lab = LabAssistants_Controller.create_lab_assistant(session, lab_assistant_data)
    # 3. Вернуть публичную версию лаборанта
    return created_lab # FastAPI автоматически преобразует SQLModel в LabAssistantPublic

# --- ЕДИНСТВЕННЫЙ Эндпоинт для авторизации лаборанта ---
@app.post("/lab_assistants/login", response_model=LabAssistantPublic)
async def login_lab_assistant_api(
    credentials: LabAssistantLogin, # Pydantic модель для входных данных (login, password)
    session: Session = Depends(get_session)
):
    # 1. Получить лаборанта по логину из БД
    lab_assistant_db = LabAssistants_Controller.get_lab_by_login_for_auth(session, credentials.login)
    # 2. Проверить существование лаборанта и верифицировать пароль
    if not lab_assistant_db or not verify_password(credentials.password, lab_assistant_db.hashed_password):
        raise HTTPException(status_code=401, detail="Incorrect login or password.")
    # 3. Если все успешно, обновить время последнего входа
    updated_lab = LabAssistants_Controller.update_lab_assistant_last_login(session, lab_assistant_db)
    # 4. Вернуть публичную версию лаборанта
    return updated_lab