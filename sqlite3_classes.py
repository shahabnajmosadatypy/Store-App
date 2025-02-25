import sqlite3
import os


def check_if_database_exists():
    name = "*.db"
    path = os.getcwd()
    print(path)
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)


print(check_if_database_exists())
