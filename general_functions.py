"""General Functions File"""

"""Clearing screen documention : https://www.geeksforgeeks.org/clear-screen-python/ """

"""import os for clearing screen"""
from os import system, name

"""Clearing Screen Functions"""


def clear_screen():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")
