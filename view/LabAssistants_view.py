from datetime import datetime
from typing import Optional, Tuple

def input_lab_data() -> Tuple[str, str, Optional[datetime], Optional[str], str]:
    """
    Коммуникация с пользователем. Заполнение информации о пользователе лаборант для регистрации
    :return:
    """
    login = input("Логин: ")
    full_name= input("ФИО: ")
    password = input("Пароль: ")
    return login, full_name, password

def entry_lab_data()-> tuple[str, str]:
    """
    Коммуникация с пользователем. Заполнение информации о пользователе лаборант для входа
    :return:
    """
    login = input("Логин: ")
    password = input("Пароль: ")
    
    return login, password

def show_add_lab_result(success):
    """
    Вывод сообщения об операции добавления лаборанта
    :param success:результат добавлния
    """
    if success:
        print("Пользователь Лаборант успешно добавлен")
    else:
        print("Ошибка при добавлении пользователя лаборанта")

# LabAssistants_view.py
def display_login_success(lab_data):
    print("\nВход успешно выполнен!")
    print(f"ID: {lab_data['id']}")
    print(f"Логин: {lab_data['login']}")
    print(f"Полное имя: {lab_data['full_name']}")
    # ... отобрази другие данные лаборанта



def display_registration_success(lab_data):
    print("Регистрация прошла успешно!")
    print(f"ID: {lab_data['id']}")
    print(f"Логин: {lab_data['login']}")
    print(f"Полное имя: {lab_data['full_name']}")

def display_register_failure(message: str = "Вход не выполнен. Лаборант уже зарегистрирован"):
    print(f"\n{message}")

# view/LabAssistants_view.py
def display_login_failure(message: str = "Вход не выполнен. Неверный логин или пароль."): # Добавь 'message' как параметр, можно с дефолтным значением
    print(f"\n{message}") # Используй переданное сообщение


def display_user_not_found():
    print("Пользователь не найден.")
# view/LabAssistants_view.py
def display_error(message: str = "Произошла неизвестная ошибка."): # Можно добавить дефолтное значение
    print(f"\nОшибка: {message}")





