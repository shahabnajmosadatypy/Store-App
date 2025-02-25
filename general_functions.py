"""General Functions File"""

"""Clearing screen documention : https://www.geeksforgeeks.org/clear-screen-python/ """

"""import os for clearing screen"""
from os import system, name

"""import time for a little sleep"""
from time import sleep

"""Clearing Screen function"""


def clear_screen():
    if name == "nt":
        _ = system("cls")
        sleep(1)
    else:
        _ = system("clear")
        sleep(1)


def set_password():
    pass


"""Wizard form functions"""


def wizard_form_password():
    print("Do you want to set an adminstration password?\n")
    _ = input("Y/N? ")

    def password_text_file(password):
        with open("pass.txt", mode="w") as text_file:
            text_file.write(str(password))

    try:
        if "y" in _:
            password = str(input("Please enter your password: "))
            password_text_file(password)
        elif "Y" in _:
            password = str(input("Please enter your password: "))
            password_text_file(password)
        elif "n" in _:
            clear_screen()
        elif "N" in _:
            clear_screen()
    except Exception as e:
        print("Error occurred:", e)


def wizard_form_store_name():
    print()


def wizard_form_three():
    print()


def wizard_form_four():
    print()


def login():
    pass
