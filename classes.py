import sqlite3


class Employees:
    def __init__(
        self, employee_code, first_name, last_name, phone_number, total_sales=0
    ):
        self.employee_code = employee_code
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.total_sales = total_sales

    def save_to_db(self):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT OR REPLACE INTO employees 
            (employee_code, first_name, last_name, phone_number, total_sales)
            VALUES (?, ?, ?, ?, ?)
        """,
            (
                self.employee_code,
                self.first_name,
                self.last_name,
                self.phone_number,
                self.total_sales,
            ),
        )
        conn.commit()
        conn.close()

    @classmethod
    def load_from_db(cls):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM employees")
        rows = cursor.fetchall()
        conn.close()

        employees = [cls(*row) for row in rows]
        return employees if employees else None

    def update_db(self, column, value):
        valid_columns = {"first_name", "last_name", "phone_number", "total_sales"}
        if column in valid_columns:
            conn = sqlite3.connect("database.db")
            cursor = conn.cursor()
            cursor.execute(
                f"UPDATE employees SET {column} = ? WHERE employee_code = ?",
                (value, self.employee_code),
            )
            conn.commit()
            conn.close()


class CustomerAccount:
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

    def save_to_db(self):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT OR REPLACE INTO customer_accounts 
            (user_name, first_name, last_name, national_code, phone_number, total_purchase, discount_amount, debt_amount)
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

    @classmethod
    def load_from_db(cls):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM customer_accounts")
        rows = cursor.fetchall()
        conn.close()

        customers = [cls(*row) for row in rows]
        return customers if customers else None

    def update_db(self, column, value):
        valid_columns = {
            "first_name",
            "last_name",
            "phone_number",
            "total_purchase",
            "discount_amount",
            "debt_amount",
        }
        if column in valid_columns:
            conn = sqlite3.connect("database.db")
            cursor = conn.cursor()
            cursor.execute(
                f"UPDATE customer_accounts SET {column} = ? WHERE user_name = ?",
                (value, self.user_name),
            )
            conn.commit()
            conn.close()


class Product:
    def __init__(self, product_code, product_name, product_price, in_stock_amount):
        self.product_code = product_code
        self.product_name = product_name
        self.product_price = product_price
        self.in_stock_amount = in_stock_amount

    def save_to_db(self):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT OR REPLACE INTO products 
            (product_code, product_name, product_price, in_stock_amount)
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

    @classmethod
    def load_from_db(cls):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products")
        rows = cursor.fetchall()
        conn.close()
        products = [cls(*row) for row in rows]
        return products

    def update_db(self, column, value):
        valid_columns = {"product_name", "product_price", "in_stock_amount"}
        if column in valid_columns:
            conn = sqlite3.connect("database.db")
            cursor = conn.cursor()
            cursor.execute(
                f"UPDATE products SET {column} = ? WHERE product_code = ?",
                (value, self.product_code),
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
        is_delivered,
    ):
        self.order_no = order_no
        self.product_code = product_code
        self.order_price = order_price
        self.order_date = order_date
        self.delivery_date = delivery_date
        self.is_delivered = is_delivered

    def save_to_db(self):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT OR REPLACE INTO orders 
            (order_no, product_code, order_price, order_date, delivery_date, is_delivered)
            VALUES (?, ?, ?, ?, ?, ?)
        """,
            (
                self.order_no,
                self.product_code,
                self.order_price,
                self.order_date,
                self.delivery_date,
                self.is_delivered,
            ),
        )
        conn.commit()
        conn.close()

    @classmethod
    def load_from_db(cls):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM orders")
        rows = cursor.fetchall()
        conn.close()

        orders = [cls(*row) for row in rows]
        return orders if orders else None

    def update_db(self, column, value):
        valid_columns = {
            "product_code",
            "order_price",
            "order_date",
            "delivery_date",
            "is_delivered",
        }
        if column in valid_columns:
            conn = sqlite3.connect("database.db")
            cursor = conn.cursor()
            cursor.execute(
                f"UPDATE orders SET {column} = ? WHERE order_no = ?",
                (value, self.order_no),
            )
            conn.commit()
            conn.close()
