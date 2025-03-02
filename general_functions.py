"""General Functions File"""

"""Clearing screen documention : https://www.geeksforgeeks.org/clear-screen-python/ """
"""SQLite3 documention : https://www.geeksforgeeks.org/python-sqlite/"""

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

            employyes = Employees(employee_code, first_name, last_name, phone_number)
            employyes.save_to_db()
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
            products.save_to_db()
            clear_screen()
    else:
        print("Error in entering product numbers, Please reload app")
        clear_screen()


"""Reading password functions"""


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


"""Documentation Links below:
https://www.w3schools.com/python/python_strings.asp
https://symbl.cc/en/unicode-table/"""


def home_page(access_level):
    while True:
        try:
            welcome_message = "Welcome to the configuration panel"
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
                len(welcome_message),
                len(functions_list),
                *(len(option) for option in options),
            )
            border = "─" * (max_length + 2)

            print(f"┌{border}┐")
            print(f"│ {welcome_message.ljust(max_length)} │")
            print(f"│ {functions_list.ljust(max_length)} │")
            for option in options:
                print(f"│ {option.ljust(max_length)} │")
            print(f"└{border}┘")
            selected_functions = int(input("Enter your function: "))
            if selected_functions == 1:
                if access_level != "1":
                    clear_screen()
                    print("Access Denied")
                    print("If you want to register an employee Please Login Now")
                    sleep(5)
                    clear_screen()
                    break
                register_employee()
                break
            elif selected_functions == 2:
                register_customer()
                break
            elif selected_functions == 3:
                if access_level != "1":
                    clear_screen()
                    print("Access Denied")
                    print("If you want to register an employee Please Login Now")
                    sleep(5)
                    clear_screen()
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
                if access_level != "1":
                    clear_screen()
                    print("Access Denied")
                    print("If you want to register an order Please Login Now")
                    sleep(5)
                    clear_screen()
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


"""Login Form"""


def login():
    print("Welcome\n")
    print("If you are adminstrator press 1 then press enter\n")
    print("If you are salesman or saleswoman press any key \n")
    user = str(input())
    if user == "1":
        clear_screen()
        read_admin_password_login()
        home_page(user)
    else:
        clear_screen()
        home_page(user)


"""Functions Panel"""


def register_employee():
    first_name = str(input("Enter your employee first name: "))
    clear_screen()
    last_name = str(input("Enter your employee last name: "))
    clear_screen()
    phone_number = str(input("Enter your employee phone number: "))
    clear_screen()
    employee_code = str(input("Make a code for your employee: "))
    emp = Employees(employee_code, first_name, last_name, phone_number)
    emp.save_to_db()
    sleep(5)
    clear_screen()
    home_page()


def register_customer():
    user_name = str(input("Enter your customer username: "))
    clear_screen()
    first_name = str(input("Enter your customer first name: "))
    clear_screen()
    last_name = str(input("Enter your customer last name: "))
    clear_screen()
    natinoal_code = str(input("Enter your customer national code: "))
    clear_screen()
    phone_number = str(input("Enter your customer phone_number: "))
    clear_screen()
    total_purchase = str(input("Enter your customer total purchases: "))
    clear_screen()
    discount_amount = str(input("Enter your customer discount amount: "))
    clear_screen()
    debt_amount = str(
        input("Does your customer have a debt? If yes enter If not enter 0")
    )
    csm = CustomerAccount(
        user_name,
        first_name,
        last_name,
        natinoal_code,
        total_purchase,
        discount_amount,
        debt_amount,
    )
    csm.save_to_db()
    sleep(5)
    clear_screen()
    home_page()


def change_employee():
    employees = Employees.load_from_db()

    if not employees:
        print("No employees found in the database.")
        return

    for employee in employees:
        print("-" * 30)
        print(f"Employee Code: {employee.employee_code}")
        print(f"First Name: {employee.first_name}")
        print(f"Last Name: {employee.last_name}")
        print(f"Phone Number: {employee.phone_number}")
        print(f"Total Sales: {employee.total_sales}")

    employee_code = input("\nEnter employee code to edit: ").strip()

    selected_employee = None
    for employee in employees:
        if str(employee.employee_code) == str(employee_code):
            selected_employee = employee
            break

    if not selected_employee:
        print("Employee not found!")
        return

    print("\nWhich field do you want to update?")
    print("1. First Name")
    print("2. Last Name")
    print("3. Phone Number")
    print("4. Total Sales")

    columns = {
        "1": "first_name",
        "2": "last_name",
        "3": "phone_number",
        "4": "total_sales",
    }
    choice = input("Enter your choice (1-4): ").strip()

    if choice not in columns:
        print("Invalid choice!")
        return

    column = columns[choice]
    new_value = input(f"Enter new value for {column}: ").strip()

    if column == "total_sales":
        try:
            new_value = float(new_value)
        except ValueError:
            print("Invalid input! Please enter a valid number for total sales.")
            return

    selected_employee.update_db(column, new_value)
    print("Employee updated successfully!")
    sleep(5)
    clear_screen()
    home_page()


def change_customer():
    customers = CustomerAccount.load_from_db()

    if not customers:
        print("No customers found in the database.")
        return

    for customer in customers:
        print("-" * 30)
        print(f"User Name: {customer.user_name}")
        print(f"First Name: {customer.first_name}")
        print(f"Last Name: {customer.last_name}")
        print(f"National Code: {customer.national_code}")
        print(f"Phone Number: {customer.phone_number}")
        print(f"Total Purchase: {customer.total_purchase}")
        print(f"Discount Amount: {customer.discount_amount}")
        print(f"Debt Amount: {customer.debt_amount}")

    user_name = input("\nEnter username to edit: ").strip()

    selected_customer = None
    for customer in customers:
        if str(customer.user_name) == str(user_name):
            selected_customer = customer
            break

    if not selected_customer:
        print("Customer not found!")
        return

    print("\nWhich field do you want to update?")
    print("1. First Name")
    print("2. Last Name")
    print("3. Phone Number")
    print("4. Total Purchase")
    print("5. Discount Amount")
    print("6. Debt Amount")

    columns = {
        "1": "first_name",
        "2": "last_name",
        "3": "phone_number",
        "4": "total_purchase",
        "5": "discount_amount",
        "6": "debt_amount",
    }
    choice = input("Enter your choice (1-6): ").strip()

    if choice not in columns:
        print("Invalid choice!")
        return

    column = columns[choice]
    new_value = input(f"Enter new value for {column}: ").strip()

    if column in ["total_purchase", "discount_amount", "debt_amount"]:
        try:
            new_value = float(new_value)
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            return

    selected_customer.update_db(column, new_value)
    print("Customer updated successfully!")
    sleep(5)
    clear_screen()
    home_page()


def register_product():
    product_code = str(input("Enter your product code: "))
    clear_screen()
    product_name = str(input("Enter your product name: "))
    clear_screen()
    product_price = str(input("Enter your product price: "))
    clear_screen()
    in_stock_amount = str(input("Enter your product amount of stock"))
    pd = Product(product_code, product_name, product_price, in_stock_amount)
    pd.save_to_db()
    sleep(5)
    clear_screen()
    home_page()


def change_product():
    products = Product.load_from_db()

    if not products:
        print("No products found in the database.")
        return

    for product in products:
        print("-" * 30)
        print(f"Product Code: {product.product_code}")
        print(f"Product Name: {product.product_name}")
        print(f"Product Price: {product.product_price}")
        print(f"In Stock Amount: {product.in_stock_amount}")

    product_code = input("\nEnter product code to edit: ").strip()

    selected_product = None
    for product in products:
        if str(product.product_code) == str(product_code):
            selected_product = product
            break

    if not selected_product:
        print("Product not found!")
        return

    print("\nWhich field do you want to update?")
    print("1. Product Name")
    print("2. Product Price")
    print("3. In Stock Amount")

    columns = {"1": "product_name", "2": "product_price", "3": "in_stock_amount"}
    choice = input("Enter your choice (1-3): ").strip()

    if choice not in columns:
        print("Invalid choice!")
        return

    column = columns[choice]
    new_value = input(f"Enter new value for {column}: ").strip()

    selected_product.update_db(column, new_value)
    print("Product updated successfully!")

    sleep(5)
    clear_screen()
    home_page()


def register_order():
    order_no = str(input("Enter your order number: "))
    clear_screen()
    product_code = str(input("Enter your product code: "))
    clear_screen()
    order_price = str(input("Enter your order price: "))
    clear_screen()
    order_date = str(input("When is order date? : "))
    clear_screen()
    delivery_date = str(input("When is delivery date? : "))
    clear_screen()
    is_delivered = str(input("It is delivered? "))
    employees = Employees.load_from_db()

    if not employees:
        print("No employees found in the database!")
        return

    print("Who sold this product?")
    print("-" * 40)
    for employee in employees:
        print(
            f"Employee Code: {employee.employee_code} | Name: {employee.first_name} {employee.last_name}"
        )
    print("-" * 40)

    employee_code = str(input("Enter the employee code: ")).strip()
    clear_screen()

    selected_employee = None
    for employee in employees:
        if str(employee.employee_code) == employee_code:
            selected_employee = employee
            break

    if not selected_employee:
        print("Invalid employee code! Order not registered.")
        return

    print(
        f"Selected Employee: {selected_employee.first_name} {selected_employee.last_name} (Code: {selected_employee.employee_code})"
    )
    print(f"Previous total sales: {selected_employee.total_sales}")

    new_total_sales = str(int(selected_employee.total_sales) + 1)
    selected_employee.update_db("total_sales", new_total_sales)

    print(f"Updated total sales: {new_total_sales}")

    order = Order(
        order_no, product_code, order_price, order_date, delivery_date, is_delivered
    )
    order.save_to_db()

    print(
        f"Order {order.order_no}, with product code {order.product_code}, has been successfully saved!"
    )
    sleep(5)
    clear_screen()
    home_page()


def register_delivery():
    print("Registering delivery is not available right now")
    sleep(5)
    clear_screen()
    home_page()


def analysis_club():
    print(
        "Analysis and Customer Club is not defined right now, It will be available on updates"
    )
    sleep(5)
    clear_screen()
    home_page()
