def input_buh_data()-> tuple[str, str]:
    """
    Коммуникация с пользователем. Заполнение информации о пользователе бухгалтер
    :return:
    """
    full_name = input("ФИО: ")
    login= input("логин: ")
    return full_name, login
def show_add_buh_result(success: bool):
    """
    Вывод сообщения об операции добавления пользователя бухгалтер
    :param success:результат добавлния
    """
    if success:
        print("Пользователь бухгалтер успешно добавлен")
    else:
        print("Ошибка при добавлении пользователя бухгалтер")

def entry_buh_data()-> tuple[str, str]:
    """
    Коммуникация с пользователем. Заполнение информации о пользователе лаборант для входа
    :return:
    """
    login = input("Логин: ")
    password = input("Пароль: ")
    return login, password
