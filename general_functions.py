"""General Functions File"""

"""Clearing screen documention : https://www.geeksforgeeks.org/clear-screen-python/ """

"""import os for clearing screen"""
from os import system, name

"""import time for a little sleep"""
from time import sleep

"""import classes.py for object making"""
from classes import *

"""import random for code generation"""
from random import randint

"""Clearing Screen function"""

import database_functions

database_functions.create_DB()


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


def wizard_form_store_name():
    store_name = input("Enter your store name: ")
    with open("storename.txt", mode="w") as text_file:
        text_file.write(str(store_name))
    clear_screen()


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
            clear_screen()
        elif "Y" in _:
            password = str(input("Please enter your password: "))
            password_text_file(password)
            clear_screen()
        elif "n" in _:
            clear_screen()
        elif "N" in _:
            clear_screen()
    except Exception as e:
        print("Error occurred:", e)


def wizard_form_employee_info():
    print("How many employees do you have? \n")
    employee_count = int(input())
    if employee_count > 0:
        for i in range(1, employee_count + 1):

            first_name = input(f"Please enter your employee number {i} first name: ")
            last_name = input(f"Please enter your employee number {i} last name: ")
            phone_number = input(
                f"Please enter your employee number {i} phone number: "
            )
            employee_code = str(randint(1, 999))

            employyes = Employyes(first_name, last_name, phone_number, employee_code)
            employyes.savetoDB()
            clear_screen()
    else:
        print("Hire employees")


def wizard_form_material_info():
    print()


def login():
    pass


wizard_form_employee_info()
