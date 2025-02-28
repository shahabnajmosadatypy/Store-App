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


def clear_screen():
    if name == "nt":
        _ = system("cls")
        sleep(1)
    else:
        _ = system("clear")
        sleep(1)


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
        if "y" in _.lower():
            password = str(input("Please enter your password: "))
            password_text_file(password)
            clear_screen()
        elif "n" in _.lower():
            clear_screen()
    except Exception as e:
        print("Error occurred:", e)


def read_admin_password_login():
    try:
        with open("pass.txt", mode="r") as text_file:
            correct_password = text_file.read().strip()
        while True:
            password = input("Enter your password: ")
            if password == correct_password:
                print("Welcome")
                sleep(2)
                clear_screen()
                break
            else:
                print("Your password was incorrect. Try again.")
    except:
        print("An error has been occurred!")


def wizard_form_employee_info():
    print("How many employees information you want to enter? \n")
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
        clear_screen()


def wizard_form_material_info():
    print("How many products do you want to enter? \n")
    product_count = int(input())
    if product_count > 0:
        for i in range(1, product_count + 1):

            product_code = input("Please enter your product code number: ")
            product_name = input("Please enter your product name: ")
            product_price = input("Please enter your product price: ")
            in_stock_amount = str(input("Please enter your amount in stock: "))

            products = Product(
                product_code, product_name, product_price, in_stock_amount
            )
            products.savetoDB()
            clear_screen()
    else:
        print("Error in entering product numbers, Please reload app")
        clear_screen()


def wizard_form_customer_info():
    pass


def home_page():
    text = ""
    border = "─" * (len(text) + 2)
    print(f"┌{border}┐")
    print(f"│ {text} │")
    print(f"│ {text} │")
    print(f"│ {text} │")
    print(f"└{border}┘")


def login():
    print(
        "Welcome\n",
        "If you are adminstrator press 1 then press enter\n",
        "If you are user press any key 2 then enter\n",
    )
    _ = str(input())
    if _ == "1":
        read_admin_password_login()
        home_page()
    else:
        clear_screen()


login()
