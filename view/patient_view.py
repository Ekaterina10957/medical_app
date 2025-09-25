def input_patient_data()->tuple[str, str, str, str, str, str, str, str, str, str, str, str, str]:
    """
    Функция для коммуникации с пациентом. Заполнение информации об пациенте.
    :return: Возвращает кортеж данных об пациенте
    """
    login = input("логин: ")
    password = input("пароль: ")
    full_name = input("ФИО: ")
    birthdate = input("дата рождения: ")
    passport_series = input("серия пасспорта:")
    passport_number = input("номер пасспорта:")
    phone = input("телефон: ")
    email = input("e-mail: ")
    insurance_number = input("Номер страхового полиса: ")
    insurance_type = input("тип страхового полиса: ")
    insurance_company_id = input(" страховая компания: ")

    return (login, password, full_name, birthdate, passport_series, passport_number, phone, email, insurance_number, insurance_type, insurance_company_id)
    
def show_add_patient_result(success: bool) -> None:
    """
    Вывод сообщения об операции добавления пациента в бд
    :param success: результат добавления
    :return: пишет сообщение в консоль
    """

    if success:
        print("Пациент успешно добавлен")
    else:
        print("Ошибка при добавлении пациента, проверьте данные пациента")

def show_info_patient_by_pass(tuple_data_patient: tuple[str, str]) -> None:
    """
    Функция для вывода информации об пациенте по его паспорту
    :param tuple_data_client: кортеж со всеми данными об пациенте
    :return: None
    """

    
    if not tuple_data_patient:
        return

    print("Данные пациента: ")
    print(f"""ID: {tuple_data_patient[0]}, 
Логин: {tuple_data_patient[1]}, 
Пароль: {tuple_data_patient[2]}, 
ФИО: {tuple_data_patient[3]}, 
дата рождения: {tuple_data_patient[4]}, 
серия паспорта: {tuple_data_patient[5]}, 
номер паспорта: {tuple_data_patient[6]}, 
телефон: {tuple_data_patient[7]}, 
e-mail: {tuple_data_patient[8]}, 
номер страхового полиса: {tuple_data_patient[9]}, 
тип страхового полиса: {tuple_data_patient[10]}, 
страховая компани: {tuple_data_patient[11]}
    """)

def input_patient_pass_by_delete():
    """
    Ввод информации (номера паспорта) для удаления пациента из базы данных
    :return: корректную серию и номер паспорта пациента для удаления 
    """

    passport_data = input("номер пасспорта:")
    return passport_data

def show_delete_patient_result(success: bool) -> None:
    """
    Вывод сообщения об операции удаления пациента из базы
    :param success: результат удаления 
    :return: вывод строки
    """

    # Если удаление получилось
    if success:
        print("Данные об пациенте успешно удалены из базы данных")
    else:
        print("При удалении данных об пациенте возникла ошибка")

def input_patient_phone():
    """
    ввод телефона пациента, которого нужно бновить 
    """
    phone_patient = input("введите телефон пациента, который хотите обновить: ")
    return phone_patient


def show_input_patient_phone(d: bool) -> None:
    """
    Вывод сообщения об операции обновления телефона пациента из базы
    :param success: результат обновления 
    :return: вывод строки
    """

    # Если удаление получилось
    if d:
        print("номер телефона пациенте успешно обновленвиз базе данных")
    else:
        print("При обновлении номера телефона пациента возникла ошибка")