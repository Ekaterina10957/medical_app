from typing import Optional
from datetime import date
from sqlmodel import Session, select
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy import create_engine
from datetime import datetime
from model.patient import Patient  
from db.database import engine

#синхронная версия
def add_patient_to_db(
    login: str,
    password: str,
    full_name: str,
    birthdate: date,  # Изменено на date
    passport_series: str,
    passport_number: str,
    phone: str,
    email: str, # Тип должен быть str
    insurance_number: str,
    insurance_type: str,
    insurance_company_id: int, # Убедитесь, что insurance_company_id является int
    
) -> bool:
    """Регистрация пациента."""
    try:
        with Session(engine) as session:
            # Создаем экземпляр Patient
            new_patient = Patient(
                login=login,
                password=password,
                full_name=full_name,
                birthdate=birthdate,  # Теперь birthdate имеет тип date
                passport_series=passport_series,
                passport_number=passport_number,
                phone=phone,
                email=email,
                insurance_number=insurance_number,
                insurance_type=insurance_type,
                insurance_company_id=insurance_company_id,
            )

            # Добавляем пациента в сессию и сохраняем в базу данных
            session.add(new_patient)
            session.commit()
            return True
    except Exception as e:
        print(f"Error adding patient to database: {e}")  # Логирование ошибки
        return False

def delete_patient(passport_number: str, engine: create_engine) -> bool:
    """Удаление данных о пациенте."""
    try:
        with Session(engine) as session:
            # Находим пациента по номеру паспорта
            patient = select(Patient).filter(Patient.passport_number == passport_number).first()

            if patient:
                # Если пациент найден, удаляем его
                session.delete(patient)
                session.commit()
                return True
            else:
                # Если пациент не найден, возвращаем False
                return False
    except Exception as e:
        print(f"Error deleting patient: {e}")
        return False
    
def update_patient_phone(phone_patient: str, engine: create_engine) -> bool:
    """Обновляет номер телефона пациента, устанавливая новый номер '344'."""
    try:
        with Session(engine) as session:
            # Ищем всех пациентов с указанным старым номером телефона
            patients_to_update = select(Patient).filter(Patient.phone == phone_patient).all()

            if patients_to_update:
                # Обновляем номер телефона для каждого найденного пациента
                for patient in patients_to_update:
                    patient.phone = "344"
                session.commit()  # Фиксируем изменения в базе данных
                return True  # Возвращаем True, если хотя бы один пациент был обновлен
            else:
                # Не найдено пациентов с указанным номером телефона
                print(f"No patients found with phone number: {phone_patient}")
                return False
    except Exception as e:
        print(f"Error updating patient phone number: {e}")  # Добавлено логирование ошибки
        return False