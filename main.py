import sqlite3_functions

while True:
    status = True
    try:
        if sqlite3_methods.check_if_database_exists == True:
            print("We have a db")
    except:
        if sqlite3_methods.check_if_database_exists == False:
            print("We dont have a db")
        status = False
    break
