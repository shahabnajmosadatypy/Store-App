""" Files Functions
This script allows to check in files
Function are based on glob and sqlite3 
"""

import sqlite3
import glob

"""Checking Functions to search for a Database"""


def check_if_database_exists():
    """
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


"""Checking function to search for password file"""


def check_if_pass_file_exists():
    """
    Documention link is below :
    https://www.geeksforgeeks.org/file-searching-using-python/

    """

    """A list for files"""
    results = []

    """Define files"""

    files = glob.glob("pass.txt")

    """Searching in files whether a file extension is .db"""

    for file in files:
        results.append(file)

    """Calling back the results of search"""
    if len(results) == 0:
        return False
    elif len(results) != 0:
        return True


"""Creating Database for first time function"""


def create_DB():
    """Make a connection to sqlite3 database"""
    conn = sqlite3.connect("database.db")

    """Make a cursor to sqlite3 database connection"""
    cursor = conn.cursor()

    """Creating tables for first time"""

    cursor.execute(
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
    cursor.execute(
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

    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS products (
        product_code TEXT PRIMARY KEY,
        product_name TEXT NOT NULL,
        product_price REAL NOT NULL,
        in_stock_amount INTEGER NOT NULL
    )
"""
    )

    cursor.execute(
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

    """Finialize changes"""
    conn.commit()

    """Closing connection to database"""
    conn.close()


"""Read from database"""


def readfromDB():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM employees""")
    result = cursor.fetchall()
    conn.commit()
    conn.close()
    return result
