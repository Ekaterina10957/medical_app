from fastapi import FastAPI, HTTPException, Depends
from sqlmodel import Session # Убедись, что это 'from sqlmodel import Session'
from model.LabAssistants import LabAssistants # Предполагаем, что файл называется lab_assistants.py в папке models
from model.Administrators import Administrator
from controller.LabAssistants_Controller import LabAssistants_Controller, get_password_hash, verify_password
from controller.Administrators_controllers import Administrators_controllers,get_password_hash, verify_password
from db.database import get_session, init_db
from schemas.LabAssistant import LabAssistantCreate, LabAssistantLogin, LabAssistantPublic 
from schemas.Administrators import AdministratorsPublic, AdministratorsCreate, AdministratorsLogin
from datetime import datetime

app = FastAPI()

# --- Хук для инициализации БД при старте приложения ---
@app.on_event("startup")
def on_startup():
    init_db()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Medical Analysis API!"}

#Эндпоинт для регистрации лаборанта 
@app.post("/lab_assistants/register", response_model=LabAssistantPublic, status_code=200)
async def register_lab_assistant_api(
    lab_assistant_data: LabAssistantCreate,
    session: Session = Depends(get_session) 
):
    existing_lab = LabAssistants_Controller.get_lab_by_login_for_auth(session, lab_assistant_data.login)
    if existing_lab:
        raise HTTPException(status_code=400, detail="Login already registered.")
    created_lab = LabAssistants_Controller.create_lab_assistant(session, lab_assistant_data)
    return created_lab

#Эндпоинт для авторизации лаборанта
@app.post("/lab_assistants/login", response_model=LabAssistantPublic)
async def login_lab_assistant_api(
    credentials: LabAssistantLogin, 
    session: Session = Depends(get_session)
):
    lab_assistant_db = LabAssistants_Controller.get_lab_by_login_for_auth(session, credentials.login)
    if not lab_assistant_db or not verify_password(credentials.password, lab_assistant_db.hashed_password):
        raise HTTPException(status_code=401, detail="Incorrect login or password.")
    updated_lab = LabAssistants_Controller.update_lab_assistant_last_login(session, lab_assistant_db)
    return updated_lab


# Эндпоинт для регистрации администратора 
@app.post("/admin/register",response_model= AdministratorsPublic, status_code= 200) 
async def administrators_register_api(
        administrators_data: AdministratorsCreate,
        session: Session = Depends(get_session)
):
    existing_admin = Administrators_controllers.get_admin_by_login_for_auth(session, administrators_data.login)
    if existing_admin:
        raise HTTPException(status_code=400, detail="Login already registered.")
    created_admin = Administrators_controllers.create_administrators(session, administrators_data)
    return created_admin


#Эндпоинт для входа администратора 
@app.post("/admin/login", response_model=AdministratorsPublic)
async def login_admin_assistant_api(
    credentials: AdministratorsLogin,
    session: Session = Depends(get_session)
):
    admin_db = Administrators_controllers.get_admin_by_login_for_auth(session, credentials.login)
    if not admin_db or not verify_password(credentials.password, admin_db.hashed_password):
        raise HTTPException(status_code=401, detail="Incorrect login or password.")
    updated_admin = Administrators_controllers.update_admin_last_login(session, admin_db)
    return updated_admin