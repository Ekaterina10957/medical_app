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
    return login_admin, password
def show_add_admin_result(success: bool):
    """
    Вывод сообщения об операции добавления пользователя администратор
    :param success:результат добавлния
    """
    if success:
        print("Пользователь администратор успешно добавлен")
    else:
        print("Ошибка при добавлении пользователя администратор")
