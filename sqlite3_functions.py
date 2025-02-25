""" SQLite3 Custom
This file allows the program to create, modify, delete and etc on Database
Based on sqlite3 with using import sqlite3
"""

import sqlite3
import os
import glob


def check_if_database_exists():
    """
    # name = "shahab.db"
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


""""""


def load_database():
    pass


print(str(check_if_database_exists()))
