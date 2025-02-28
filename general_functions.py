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


"""Documentation Links below:
https://www.w3schools.com/python/python_strings.asp
https://symbl.cc/en/unicode-table/"""


def home_page():
    welcome_message = "Welcome to the administrator panel"
    functions_list = "Available Functions:"
    options = [
        "1. Register an employee",
        "2. Register a customer",
        "3. Change an employee specifications",
        "4. Change a customer specifications",
        "5. Register a new product",
        "6. Change product details",
        "7. Register an order",
        "8. Register a delivery",
        "9. Analyze Sales and Customer Club",
    ]
    max_length = max(
        len(welcome_message), len(functions_list), *(len(option) for option in options)
    )
    border = "─" * (max_length + 2)

    print(f"┌{border}┐")
    print(f"│ {welcome_message.ljust(max_length)} │")
    print(f"│ {functions_list.ljust(max_length)} │")
    for option in options:
        print(f"│ {option.ljust(max_length)} │")
    print(f"└{border}┘")
    while True:
        try:
            selected_functions = int(input("Enter your function: "))
            if selected_functions == 1:
                register_employee()
                break
            elif selected_functions == 2:
                register_customer()
                break
            elif selected_functions == 3:
                change_employee()
                break
            elif selected_functions == 4:
                change_customer()
                break
            elif selected_functions == 5:
                register_product()
                break
            elif selected_functions == 6:
                change_product()
                break
            elif selected_functions == 7:
                register_order()
                break
            elif selected_functions == 8:
                register_delivery()
                break
            elif selected_functions == 9:
                analysis_club()
                break
            else:
                clear_screen()
                print("An error has occurred")
        except:
            print("Invalid input. Please enter a number.")


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


"""Adminstrator Functions Panel"""


def register_employee():
    pass


def register_customer():
    pass


def change_employee():
    pass


def change_customer():
    pass


def register_product():
    pass


def change_product():
    pass


def register_order():
    pass


def register_delivery():
    pass


def analysis_club():
    pass


home_page()
