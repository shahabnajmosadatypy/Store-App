import sqlite3_functions

while True:
    status = True
    try:
        if sqlite3_functions.check_if_database_exists():
            status = True
        else:
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
        wizard = input("Yes/No? ")
        try:
            if "y" in wizard:
                pass
            elif "n" in wizard:
                pass
            elif "Y" in wizard:
                pass
            elif "N" in wizard:
                pass
        except Exception as e:
            print("Error occurred:", e)
        break
    break
