from view.LabAssistants_view import input_lab_data,entry_lab_data, show_add_lab_result, display_register_failure
from view.Administrators_view import input_admin_data, show_add_admin_result,entry_admin_data
from view.Accountants_view import input_buh_data, entry_buh_data
from view.patient_view import input_patient_data, show_add_patient_result, input_patient_pass_by_delete, show_delete_patient_result, input_patient_phone, show_input_patient_phone
from db.database import init_db
from controller import LabAssistants_Controller, Administrators_controllers, Accountants_controller,patient_Controller
from controller.LabAssistants_Controller import add_lab
from controller import patient_Controller
from view import LabAssistants_view, Accountants_view,Administrators_view
import requests
def show_lab_menu():
    """Отображает меню лаборанта."""
    print("\n--- Меню лаборанта ---")
    # Здесь будет функционал лаборанта
    while True:
        print("привет1")

def show_admin_menu():
    """Отображает меню администратора."""
    print("\n--- Меню администратора ---")
    # Здесь будет функционал администратора
    pass

def show_buh_menu():
    """Отображает меню бухгалтера."""
    print("\n--- Меню бухгалтера ---")
    # Здесь будет функционал бухгалтера
    pass

init_db()
    
while True:
        print("\n=== Главное меню ===")
        print("1. Лаборант (Регистрация/Вход)")
        print("2. Администратор (Регистрация/Вход)")
        print("3. Бухгалтер (Регистрация/Вход)")
        print("4. Регистрация нового пациента")
        print("5. Удаление данных о пациенте")
        print("6. Обновление телефона пациента")
        print("7. Выход")
        
        choice = input("Выберите действие: ")
        
        if choice == "1":
            print("1. вход")
            print("2. регистрация")
            klick =input("выберите действие: ")
            import requests 

            if klick == "1": 
                login, password = entry_lab_data()  
                api_url_lab = "http://127.0.0.1:8000/lab_assistants/login"
                payload = {"login": login, "password": password}
                try:
                    response = requests.post(api_url_lab, json=payload)
                    if response.status_code == 200:
                        lab_data = response.json() 
                        LabAssistants_view.display_login_success(lab_data)  
                        show_lab_menu()
                    elif response.status_code == 401:  
                        error_detail = response.json().get("detail", "Неверный логин или пароль.")
                        LabAssistants_view.display_login_failure(error_detail) 
                    else:  
                        LabAssistants_view.display_error(f"Ошибка API: {response.status_code} - {response.text}")
                except requests.exceptions.ConnectionError:
                    LabAssistants_view.display_error("Не удалось подключиться к API-серверу. Убедитесь, что он запущен.")
            else:
                    klick == "2"
                    login, full_name, password  = input_lab_data()
                    api_url = "http://127.0.0.1:8000/lab_assistants/login"

                    payload = {"login": login, "full_name": full_name, "password": password }
                    try:  
                        response = requests.post(api_url, json=payload)
                        if response.status_code == 201:  # Успешный вход
                            lab_data = response.json()
                            LabAssistants_view.display_registration_success(lab_data)
                            show_lab_menu()
                        elif response.status_code == 400:
                            error_detail = response.json().get("detail", "Администратор уже зарегистрирован")
                            LabAssistants_view.display_register_failure(error_detail)
                        else:
                            LabAssistants_view.display_error(f"Ошибка API: {response.status_code} - {response.text}")
                    except requests.exceptions.ConnectionError:
                        LabAssistants_view.display_error("Не удалось подключиться к API-серверу. Убедитесь, что он запущен.")
                #if "успешно добавлен" in success:
                    #show_lab_menu()
                
        elif choice == "2":
            print("1. вход")
            print("2. регистрация")
            klick =input("выберите действие: ")
            if klick == "1":  # Вход
                login, password = entry_admin_data()
                api_url_admin = "http://127.0.0.1:8000/admin/login"
                admin_json = {"login": login, "password":password}
                try:
                    response = requests.post(api_url_admin, json=admin_json)
                    if response.status_code == 200:  
                        admin_data = response.json()  
                        Administrators_view.display_login_success(admin_data)
                        show_admin_menu()
                    elif response.status_code == 401: 
                        error_detail = response.json().get("detail", "Неверный логин или пароль.")
                        Administrators_view.login_failure(error_detail) 
                    else:  
                        Administrators_view.display_error(f"Ошибка API: {response.status_code} - {response.text}")
                except requests.exceptions.ConnectionError:
                    Administrators_view.display_error("Не удалось подключиться к API-серверу. Убедитесь, что он запущен.")
            else:
                klick == "2"
                login, password, phone = input_admin_data()
                admin_api_url = "http://127.0.0.1:8000/admin/register"
                admin_json = {"login": login, "password":password, "phone": phone}
                try:  
                        response = requests.post(admin_api_url, json=admin_json)
                        if response.status_code == 200:  
                            admin_data = response.json()
                            Administrators_view.display_registration_success(admin_data)
                            show_admin_menu()
                        elif response.status_code == 400:
                            error_detail = response.json().get("detail", "Администратор уже зарегистрирован")
                            Administrators_view.display_register_failure(error_detail)
                        else:
                            Administrators_view.display_error(f"Ошибка API: {response.status_code} - {response.text}")
                except requests.exceptions.ConnectionError:
                        Administrators_view.display_error("Не удалось подключиться к API-серверу. Убедитесь, что он запущен.")
                
        elif choice == "3":
            print("1. вход")
            print("2. регистрация")
            klick =input("выберите действие: ")
            if klick == "1":  # Вход
                login, password = entry_buh_data()
                api_url_accuntant = "http://127.0.0.1:8000/accountant/login"
                accuntant_json = {"login": login, "password":password}
                try:
                    response = requests.post(api_url_accuntant, json=accuntant_json)
                    if response.status_code == 200:  
                        accuntant_data = response.json()  
                        Accountants_view.display_login_success(accuntant_data)
                        show_buh_menu()
                    elif response.status_code == 401: 
                        error_detail = response.json().get("detail", "Неверный логин или пароль.")
                        Accountants_view.login_failure(error_detail) 
                    else:  
                        Accountants_view.display_error(f"Ошибка API: {response.status_code} - {response.text}")
                except requests.exceptions.ConnectionError:
                    Accountants_view.display_error("Не удалось подключиться к API-серверу. Убедитесь, что он запущен.")
            else:
                klick == "2"
                login, password, full_name = input_buh_data()
                api_url_accuntant = "http://127.0.0.1:8000/accountant/register"
                accuntant_json = {"login": login, "password":password, "full_name": full_name}
                try:  
                        response = requests.post(api_url_accuntant, json=accuntant_json)
                        if response.status_code == 200:  
                            accuntant_data = response.json()
                            Accountants_view.display_registration_success(accuntant_data)
                            show_buh_menu()
                        elif response.status_code == 400:
                            error_detail = response.json().get("detail", "Бухгалтер уже зарегистрирован")
                            Accountants_view.display_register_failure(error_detail)
                        else:
                            Accountants_view.display_error(f"Ошибка API: {response.status_code} - {response.text}")
                except requests.exceptions.ConnectionError:
                        Accountants_view.display_error("Не удалось подключиться к API-серверу. Убедитесь, что он запущен.")
                
                
        elif choice == "4":
            tuple_of_data = input_patient_data()
            success = patient_Controller.add_patient_to_db(*tuple_of_data)
            show_add_patient_result(success)
            
        elif choice == "5":
            print("Ниже введите данные о пациенте для удаления его из базы данных.")
            passport_number_of_patient = input_patient_pass_by_delete()
            success_delete = patient_Controller.delete_patient(passport_number_of_patient)
            show_delete_patient_result(success_delete)
            
        elif choice == "6":
            phone_patient = input_patient_phone()
            result = patient_Controller.update_patient_phone(phone_patient)
            show_input_patient_phone(result)
            
        elif choice == "7":
            print("Выход из программы")
            break
            
        else:
            print("Неверный выбор")




