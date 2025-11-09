import psycopg2
from model.Administrators import Administrator
from argon2 import PasswordHasher,exceptions as argon2_exceptions
from typing import Optional
from datetime import date, datetime
from sqlmodel import Session, select
from db.database import engine
from passlib.hash import argon2
from schemas.Administrators import AdministratorsCreate


ph = argon2.using(rounds=4) 

def get_password_hash(password: str) -> str:
    """Хеширует пароль."""
    return ph.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Проверяет нехешированный пароль на соответствие хешированному."""
    try:
        ph.verify(hashed_password, plain_password)
        return True
    except argon2_exceptions.VerifyMismatchError:
        return False
    


class Administrators_controllers:
    @staticmethod
    def get_admin_by_login_for_auth(session: Session, login: str) -> Optional[Administrator]:
        """
        Ищет админитсратора по логину для целей авторизации (получения хешированного пароля).
        Не проверяет пароль.
        """
        statement = select(Administrator).where(Administrator.login == login)
        return session.exec(statement).first()
    @staticmethod
    def create_administrators(session: Session, admin_data: AdministratorsCreate) -> Administrator:
        """
        Регистрирует нового администратора.
        Принимает AdministratorsCreate, хеширует пароль и сохраняет в БД.
        """
        hashed_password = get_password_hash(admin_data.password)
        
        db_administrators = Administrator(
            login=admin_data.login,
            hashed_password=hashed_password,
            phone=admin_data.phone
        )
        
        session.add(db_administrators)
        session.commit()
        session.refresh(db_administrators) 
        return db_administrators
    @staticmethod
    def update_admin_last_login(session: Session, admin: Administrator) -> Administrator:
        """Обновляет время последнего входа администратора."""
        admin.last_login = datetime.utcnow()
        session.add(admin)
        session.commit()
        session.refresh(admin)
        return admin
    

def add_admin(login_data: str, phone_data: Optional[str] = None, password:str ="")->Optional[Administrator]:
    """
    Добавление клиента
    :param conn: Объект соединения с базой данных
    :param cursor: Объект курсора для выполнения SQL-запросов
    :param login: логин пользователя
    :param full_name: ФИО пользователя
    :return: True, если добавление успешно, иначе False
    """
    ph=PasswordHasher()
    hash_pass = ph.hash(password)
    with Session(engine) as session:
            adinistrator = Administrator(login=login_data, phone=phone_data, hashed_password= hash_pass)
            session.add(adinistrator)
            session.commit()
            session.refresh(adinistrator)
            return adinistrator
        #else:
            #return None
        
def get_admin_by_login(login: str, password: str):
    """
    Авторизация администратора 
    :param login: логин пользователя
    :param password: пароль пользователя
    :return: True, если авторизация успешна, иначе False
    """

    ph = PasswordHasher()
    with Session(engine) as session:
        statement = select(Administrator).where(Administrator.login == login)
        admin = session.exec(statement).first()
        if admin is None:
            return None
        try:
            ph.verify(admin.hashed_password, password)
            return admin
        except argon2_exceptions.VerifyMismatchError:
            return None
