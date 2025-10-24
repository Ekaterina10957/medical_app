from datetime import datetime
from typing import Optional, Tuple

def input_lab_data() -> Tuple[str, str, Optional[datetime], Optional[str], str]:
    """
    Коммуникация с пользователем. Заполнение информации о пользователе лаборант для регистрации
    :return:
    """
    login_data = input("Логин: ")
    full_name_data = input("ФИО: ")

    last_login_data = input("последний вход (YYYY-MM-DD HH:MM:SS, оставьте пустым, если нет): ")
    if last_login_data:
        try:
            last_login_data = datetime.strptime(last_login_data, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            print("Неверный формат даты.  Значение будет пропущено.")
            last_login_data = None
    else:
        last_login_data = None

    services_provided_data = input("предоставляемые услуги (оставьте пустым, если нет): ")
    if not services_provided_data:
        services_provided_data = None

    password = input("Пароль: ")
    return login_data, full_name_data, last_login_data, services_provided_data, password

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

def display_login_failure():
    print("Неверный логин или пароль.")

def display_registration_success():
    print("Регистрация прошла успешно!")

# view/LabAssistants_view.py
def display_login_failure(message: str = "Вход не выполнен. Неверный логин или пароль."): # Добавь 'message' как параметр, можно с дефолтным значением
    print(f"\n{message}") # Используй переданное сообщение


def display_user_not_found():
    print("Пользователь не найден.")
# view/LabAssistants_view.py
def display_error(message: str = "Произошла неизвестная ошибка."): # Можно добавить дефолтное значение
    print(f"\nОшибка: {message}")





