def input_buh_data()-> tuple[str, str]:
    """
    Коммуникация с пользователем. Заполнение информации о пользователе бухгалтер
    :return:
    """
    login= input("логин: ")
    full_name = input("ФИО: ")
    password  = input("Пароль: ")
    

    return full_name, login,password

def entry_buh_data()-> tuple[str, str]:
    """
    Коммуникация с пользователем. Заполнение информации о пользователе лаборант для входа
    :return:
    """
    login = input("Логин: ")
    password = input("Пароль: ")
    return login, password


def display_login_success(accuntant_data):
            print("\nВход успешно выполнен!")
            print(f"ID: {accuntant_data.get('id', 'N/A')}") # Используйте .get() для безопасности
            print(f"Логин: {accuntant_data.get('login', 'N/A')}")
            # print(f"Пароль: {accuntant_data['password']}") # Эту строку нужно УДАЛИТЬ или закомментировать
            # print(f"\n{message}") # 'message' не определена, удалите или определите
            print("\nДобро пожаловать!")

def login_failure(message: str = "Вход не выполнен. Неверный логин или пароль."):
    print(f"\n{message}")

def display_error(message: str = "Произошла неизвестная ошибка."): 
    print(f"\nОшибка: {message}")

def display_registration_success(accuntant_data):
    print("Регистрация прошла успешно!")
    

def display_register_failure(message: str = "Вход не выполнен. Администратор уже зарегистрирован"):
    print(f"\n{message}")