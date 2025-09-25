from model.Administrators import Administrators
from  argon2 import PasswordHasher,exceptions as argon2_exceptions
from typing import Optional
from datetime import date, datetime
from sqlmodel import Session, select
from db.database import engine
def add_admin(login_data: str, phone_data: Optional[str] = None, password:str ="")->Optional[Administrators]:
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
        # = select(Administrators).where(Administrators.login == login_data)
        #if find_admin is None:
            adinistrator = Administrators(login=login_data, phone=phone_data, hashed_password= hash_pass)
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
        statement = select(Administrators).where(Administrators.login == login)
        admin = session.exec(statement).first()
        if admin is None:
            return None
        try:
            ph.verify(admin.hashed_password, password)
            return admin
        except argon2_exceptions.VerifyMismatchError:
            return None
