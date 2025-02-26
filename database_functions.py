""" SQLite3 Custom
This script allows to check if a Database exists
Based on sqlite3 with using import sqlite3
"""

import sqlite3
import glob


def check_if_database_exists():
    """
    # name = "*.db"
    # path = os.getcwd()
    # print(path)
    # results = []
    # for root, dirs, files in os.walk(path):
    #     if name in files:
    #         results.append(os.path.join(root, name))
    # return results

    Cause of not working os.walk(path)
    I had to use glob
    Documention link is below :
    https://www.geeksforgeeks.org/file-searching-using-python/

    """

    """A list for files"""
    results = []

    """Define files"""

    files = glob.glob("*.db")

    """Searching in files whether a file extension is .db"""

    for file in files:
        results.append(file)

    """Calling back the results of search"""
    if len(results) == 0:
        return False
    elif len(results) != 0:
        return True


def create_DB():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute(
        """
    CREATE TABLE IF NOT EXISTS employees (
        employee_code TEXT,
        first_name TEXT,
        last_name TEXT,
        phone_number TEXT,
        total_sales TEXT
    )
    """
    )
    cur.execute(
        """
    CREATE TABLE IF NOT EXISTS customer_accounts (
        user_name TEXT PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        national_code TEXT UNIQUE NOT NULL,
        phone_number TEXT UNIQUE NOT NULL,
        total_purchase REAL DEFAULT 0,
        discount_amount REAL DEFAULT 0,
        debt_amount REAL DEFAULT 0
    )
"""
    )
    cur.execute(
        """
    CREATE TABLE IF NOT EXISTS products (
        product_code TEXT PRIMARY KEY,
        product_name TEXT NOT NULL,
        product_price REAL NOT NULL,
        in_stock_amount INTEGER NOT NULL
    )
"""
    )
    cur.execute(
        """
    CREATE TABLE IF NOT EXISTS orders (
        order_no INTEGER PRIMARY KEY,
        product_code TEXT NOT NULL,
        order_price REAL NOT NULL ,
        order_date TEXT NOT NULL,
        delivery_date TEXT NOT NULL,
        total_orders INTEGER NOT NULL
    )
"""
    )
    conn.commit()
    conn.close()
