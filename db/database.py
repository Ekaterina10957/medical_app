from typing import Generator
from sqlmodel import SQLModel, Session
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
load_dotenv()
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DBNAME = os.getenv("DBNAME")

if not all([DB_USER, DB_PASS, DB_HOST, DB_PORT, DBNAME]):
    raise ValueError("не все переменные Базы данных поключены")

DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DBNAME}"
engine = create_engine(DATABASE_URL, echo=True)
def init_db():
    print(f"инициализация Базы данных по URL:{DATABASE_URL}")
    SQLModel.metadata.create_all(engine)
    print("Таблицы Базы данных созданы, если не существовали ")

def close_db():
    print("Закрытие соединения с Базой данных")
    engine.dispose() # Освобождение ресурсов
    print("Соединение с Базой данных закртыто")

def get_engine():
    """Получение engine для миграций"""
    return engine

def get_session()-> Generator[Session, None, None]:
    """
    Возвращает сессию базы данных. Используется FastAPI как зависимость.
    """
    with Session(engine) as session:
        yield session # 'yield'