import database_functions
import general_functions

while True:
    status = True
    try:
        if database_functions.check_if_database_exists():
            status = True
        else:
            database_functions.create_DB()
            status = False
    except Exception as e:
        print("Error occurred:", e)
        break
    while status == True:
        pass
    while status == False:
        print(
            "Hello dear user, any previous database not found on your system?\n",
            "If you are admin, Do you want to run a wizard?\n",
            "If you are not admin program will be closed",
        )
        wizard_var = input("Yes/No? ")
        try:
            if "y" in wizard_var.lower():
                general_functions.clear_screen()
                general_functions.wizard_form_password()
                general_functions.wizard_form_store_name()
            elif "n" in wizard_var.lower():
                general_functions.clear_screen()
                break
        except Exception as e:
            print("Error occurred:", e)
        break
    break
