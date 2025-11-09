import psycopg2
from model.Accountants import Accountants
from argon2 import PasswordHasher,exceptions as argon2_exceptions
from typing import Optional
from datetime import date, datetime
from sqlmodel import Session, select
from db.database import engine
from passlib.hash import argon2
from schemas.Accountant import AccountantCreate


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
    


class Accountants_controller:
    @staticmethod
    def get_accountant_by_login_for_auth(session: Session, login: str) -> Optional[Accountants]:
        """
        Ищет бухгалтера по логину для целей авторизации (получения хешированного пароля).
        Не проверяет пароль.
        """
        statement = select(Accountants).where(Accountants.login == login)
        return session.exec(statement).first()
    @staticmethod
    def create_accountant(session: Session, accountant_data: AccountantCreate) -> Accountants:
        """
        Регистрирует нового бухгалтера.
        Принимает AccountantCreate, хеширует пароль и сохраняет в БД.
        """
        hashed_password = get_password_hash(accountant_data.password)
        
        db_accountant = Accountants(
            login=accountant_data.login,
            full_name=accountant_data.full_name,
            hashed_password=hashed_password
            
        )
        
        session.add(db_accountant)
        session.commit()
        session.refresh(db_accountant) 
        return db_accountant
    @staticmethod
    def update_accountant_last_login(session: Session, accountant:Accountants) -> Accountants:
        """Обновляет время последнего входа бухгалтера ."""
        accountant.last_login = datetime.utcnow()
        session.add(accountant)
        session.commit()
        session.refresh(accountant)
        return accountant

def add_buh(login_data:str, full_name_data: str,last_login_data:Optional[datetime] = None,billed_insurance_companies_data: Optional[str] = None, password: str ="" )->Optional[Accountants]:
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
        #find_buh = select(Accountants).where(Accountants.login == login_data)
        #if find_buh is None:
            accountants = Accountants(login_buh=login_data, full_name_buh=full_name_data,last_login_buh=last_login_data,billed_insurance_companies= billed_insurance_companies_data, hashed_password= hash_pass)
            session.add(accountants)
            session.commit()
            session.refresh(accountants)
            return accountants
        #else:
            #return None
    
def get_buh_by_login(login: str, password: str):
    """
    Авторизация лаборанта
    :param login: логин пользователя
    :param password: пароль пользователя
    :return: True, если авторизация успешна, иначе False
    """

    ph = PasswordHasher()
    with Session(engine) as session:
        statement = select(Accountants).where(Accountants.login == login)
        buh = session.exec(statement).first()
        if buh is None:
            return None
        try:
            ph.verify(buh.hashed_password, password)
            return buh
        except argon2_exceptions.VerifyMismatchError:
            return None
    