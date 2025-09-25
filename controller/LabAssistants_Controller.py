import psycopg2
from model.LabAssistants import LabAssistants
from  argon2 import PasswordHasher,exceptions as argon2_exceptions
from typing import Optional
from datetime import date, datetime
from sqlmodel import Session, select
from db.database import engine

def add_lab(login_data:str, full_name_data: str,last_login_data:Optional[datetime] = None,services_provided_data: Optional[str] = None, password: str ="" )->Optional[LabAssistants]:
    """
    регистрация лаборанта
    :param login: логин пользователя
    :param password: пароль пользователя
    :param full_name: ФИО пользователя
    :return: True, если добавление успешно, иначе False
    """
    ph=PasswordHasher()
    hash_pass = ph.hash(password)
    with Session(engine) as session:
        #find_user = select(LabAssistants).where(LabAssistants.login == login_data)
        #if find_user is None:
            Lab_Assistants = LabAssistants(login=login_data, full_name=full_name_data, last_login=last_login_data, services_provided= services_provided_data, hashed_password= hash_pass)
            session.add(Lab_Assistants)
            session.commit()
            session.refresh(Lab_Assistants)
            return Lab_Assistants
        #else:
            #return None
    
def get_lab_by_login(login: str, password: str):
    """
    Авторизация лаборанта
    :param login: логин пользователя
    :param password: пароль пользователя
    :return: True, если авторизация успешна, иначе False
    """

    ph = PasswordHasher()
    with Session(engine) as session:
        statement = select(LabAssistants).where(LabAssistants.login == login)
        lab = session.exec(statement).first()
        if lab is None:
            return None
        try:
            ph.verify(lab.hashed_password, password)
            return lab
        except argon2_exceptions.VerifyMismatchError:
            return None
    


    

