import files_functions
import general_functions

"""Git Tutorial by Atryia Academy"""


def main():
    while True:
        status = True
        try:
            if files_functions.check_if_database_exists():
                status = True
            else:
                status = False
        except Exception as e:
            print("Error occurred:", e)
            break
        while status == True:
            general_functions.login()
        while status == False:
            print(
                "Hello dear user, any previous database not found on your system?\nIf you are adminstrator, Do you want to run a wizard?"
            )
            wizard_var = input("Yes/No? ")
            try:
                if "y" in wizard_var.lower():
                    files_functions.create_DB()
                    general_functions.clear_screen()
                    general_functions.wizard_form_password()
                    general_functions.wizard_form_store_name()
                    general_functions.wizard_form_employee_info()
                    general_functions.wizard_form_material_info()
                    print("Wizard has been finished!")
                    general_functions.clear_screen()
                    general_functions.home_page()
                elif "n" in wizard_var.lower():
                    general_functions.clear_screen()
                    break
            except Exception as e:
                print("Error occurred:", e)
            break
        break


main()
