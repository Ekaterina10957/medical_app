from view.LabAssistants_view import input_lab_data,entry_lab_data, show_add_lab_result
from view.Administrators_view import input_admin_data, show_add_admin_result,entry_admin_data
from view.Accountants_view import input_buh_data, show_add_buh_result, entry_buh_data
from view.patient_view import input_patient_data, show_add_patient_result, input_patient_pass_by_delete, show_delete_patient_result, input_patient_phone, show_input_patient_phone
from db.database import init_db
from controller import LabAssistants_Controller, Administrators_controllers, Accountants_controller,patient_Controller
from controller.LabAssistants_Controller import add_lab
from controller import patient_Controller
from view import LabAssistants_view, Accountants_view
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
            if klick == "1":  # Вход
                login, password = entry_lab_data()
                if LabAssistants_Controller.get_lab_by_login(login, password):
                    LabAssistants_view.display_login_success()
                    show_lab_menu() 
                else:
                    LabAssistants_view.display_login_failure()
            else:
                klick == "2"
                login_data, full_name_data, last_login_data, services_provided_data, password  = input_lab_data()
                success = add_lab(login_data, full_name_data, last_login_data, services_provided_data, password)
                show_add_lab_result(success)
            #if "успешно добавлен" in success:
                #show_lab_menu()
                
        elif choice == "2":
            print("1. вход")
            print("2. регистрация")
            klick =input("выберите действие: ")
            if klick == "1":  # Вход
                login, password = entry_admin_data()
                if LabAssistants_Controller.get_admin_by_login(login, password):
                    LabAssistants_view.display_login_success()
                    show_admin_menu()
            else:
                klick == "2"
                login, password = input_admin_data()
                success = Administrators_controllers.add_admin(login, password)
                show_add_admin_result(success)
            #if "успешно добавлен" in success:
            #       show_admin_menu()
                
        elif choice == "3":
            print("1. вход")
            print("2. регистрация")
            klick =input("выберите действие: ")
            if klick == "1":  # Вход
                login, password = entry_buh_data()
                if Accountants_controller.get_buh_by_login(login, password):
                    Accountants_view.display_login_success()
                    show_buh_menu()
            else:
                login, full_name = input_buh_data()
                success = Accountants_controller.add_buh(login, full_name)
                show_add_buh_result(success)
                #if "успешно добавлен" in success:
                    #show_buh_menu()
                
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




