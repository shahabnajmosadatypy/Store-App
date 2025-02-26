import sqlite3


class Employyes:
    def __init__(
        self, employee_code, first_name, last_name, phone_number, total_sales=0
    ):
        self.employee_code = employee_code
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.total_sales = total_sales

    def savetoDB(self):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT OR REPLACE INTO employees (employee_code, first_name, last_name, phone_number, total_sales)
            VALUES (?, ?, ?, ?, ?)
        """,
            (
                str(self.employee_code),
                self.first_name,
                self.last_name,
                self.phone_number,
                str(self.total_sales),
            ),
        )
        conn.commit()
        conn.close()


class Customer_Account:
    def __init__(
        self,
        user_name,
        first_name,
        last_name,
        national_code,
        phone_number,
        total_purchase,
        discount_amount,
        debt_amount,
    ):
        self.user_name = user_name
        self.first_name = first_name
        self.last_name = last_name
        self.national_code = national_code
        self.phone_number = phone_number
        self.total_purchase = total_purchase
        self.discount_amount = discount_amount
        self.debt_amount = debt_amount

    def savetoDB(self):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT OR REPLACE INTO customer_accounts (user_name, first_name, last_name, national_code, phone_number, total_purchase, discount_amount, debt_amount)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
            (
                self.user_name,
                self.first_name,
                self.last_name,
                self.national_code,
                self.phone_number,
                self.total_purchase,
                self.discount_amount,
                self.debt_amount,
            ),
        )
        conn.commit()
        conn.close()


class Product:
    def __init__(self, product_code, product_name, product_price, in_stock_amount):
        self.product_code = product_code
        self.product_name = product_name
        self.product_price = product_price
        self.in_stock_amount = in_stock_amount

    def savetoDB(self):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT OR REPLACE INTO products (product_code, product_name, product_price, in_stock_amount)
            VALUES (?, ?, ?, ?)
        """,
            (
                self.product_code,
                self.product_name,
                self.product_price,
                self.in_stock_amount,
            ),
        )
        conn.commit()
        conn.close()


class Order:
    def __init__(
        self,
        order_no,
        product_code,
        order_price,
        order_date,
        delivery_date,
        total_orders,
    ):
        self.order_no = order_no
        self.product_code = product_code
        self.order_price = order_price
        self.order_date = order_date
        self.delivery_date = delivery_date
        self.total_orders = total_orders

    def savetoDB(self):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT OR REPLACE INTO orders (order_no, product_code, order_price, order_date, delivery_date, total_orders)
            VALUES (?, ?, ?, ?, ?, ?)
        """,
            (
                self.order_no,
                self.product_code,
                self.order_price,
                self.order_date,
                self.delivery_date,
                self.total_orders,
            ),
        )
        conn.commit()
        conn.close()
