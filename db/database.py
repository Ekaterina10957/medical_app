from sqlmodel import SQLModel, create_engine, Session
import os
from dotenv import load_dotenv
import psycopg2
load_dotenv()
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DBNAME = os.getenv("DBNAME")

DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DBNAME}"

engine = create_engine(DATABASE_URL, echo=True)
def init_db():
    print(DATABASE_URL)
    SQLModel.metadata.create_all(engine)
    
def get_session():
    """
    Возвращает сессию базы данных. Используется FastAPI как зависимость.
    """
    with Session(engine) as session:
        yield session # 'yield'
