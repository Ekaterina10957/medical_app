def entry_admin_data()-> tuple[str, str]:
    """
    Коммуникация с пользователем. Заполнение информации о пользователе администратор для входа
    :return:
    """
    login = input("Логин: ")
    password = input("Пароль: ")
    
    return login, password

def input_admin_data()-> tuple[str, str]:
    """
    Коммуникация с пользователем. Заполнение информации о пользователе администратор
    :return:
    """
    login_admin = input("Логин: ")
    password = input("пароль: ")
    phone = input("телефон: ")
    return login_admin, password, phone
def show_add_admin_result(admin_data):
    """
    Вывод сообщения об операции добавления пользователя администратор
    :param success:результат добавлния
    """
    print("\nВход успешно выполнен!")

def display_login_success(admin_data):
    print("\nВход успешно выполнен!")
    print(f"Логин: {admin_data['login']}")
    print(f"Пароль: {admin_data['password']}")
    print(f"Телефон: {admin_data['phone']}")

def display_registration_success(admin_data):
    print("Регистрация прошла успешно!")
    print(f"Логин: {admin_data['login']}")
    
    print(f"Телефон: {admin_data['phone']}")

def display_register_failure(message: str = "Вход не выполнен. Администратор уже зарегистрирован"):
    print(f"\n{message}")

def login_failure(message: str = "Вход не выполнен. Неверный логин или пароль."):
    print(f"\n{message}")

def display_error(message: str = "Произошла неизвестная ошибка."): 
    print(f"\nОшибка: {message}")