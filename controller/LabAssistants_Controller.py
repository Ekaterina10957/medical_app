import psycopg2
from model.LabAssistants import LabAssistants
from  argon2 import PasswordHasher,exceptions as argon2_exceptions
from typing import Optional
from datetime import date, datetime
from sqlmodel import Session, select
from db.database import engine
from passlib.hash import argon2 # Убедись, что используешь правильный хешер
from model.LabAssistants import LabAssistants # Убедись, что путь правильный
from schemas.LabAssistant import LabAssistantCreate


ph = argon2.using(rounds=4) # Создаем экземпляр Argon2PasswordHasher

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
    

class LabAssistants_Controller:
    @staticmethod
    def get_lab_by_login_for_auth(session: Session, login: str) -> Optional[LabAssistants]:
        """
        Ищет лаборанта по логину для целей авторизации (получения хешированного пароля).
        Не проверяет пароль.
        """
        statement = select(LabAssistants).where(LabAssistants.login == login)
        return session.exec(statement).first()
    @staticmethod
    def create_lab_assistant(session: Session, lab_assistant_data: LabAssistantCreate) -> LabAssistants:
        """
        Регистрирует нового лаборанта.
        Принимает LabAssistantCreate, хеширует пароль и сохраняет в БД.
        """
        hashed_password = get_password_hash(lab_assistant_data.password)
        
        db_lab_assistant = LabAssistants(
            login=lab_assistant_data.login,
            full_name=lab_assistant_data.full_name,
            hashed_password=hashed_password
            # id будет сгенерирован БД
            # last_login и services_provided будут None по умолчанию
        )
        
        session.add(db_lab_assistant)
        session.commit()
        session.refresh(db_lab_assistant) # Обновляет объект, чтобы получить сгенерированный ID
        return db_lab_assistant
    @staticmethod
    def update_lab_assistant_last_login(session: Session, lab_assistant: LabAssistants) -> LabAssistants:
        """Обновляет время последнего входа лаборанта."""
        # Убедись, что lab_assistant это уже объект из БД
        lab_assistant.last_login = datetime.utcnow() # Убедись, что datetime импортирован
        session.add(lab_assistant)
        session.commit()
        session.refresh(lab_assistant)
        return lab_assistant
    
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
    


    

