#!/usr/bin/python3

"""Contains function reads a text file
"""

def read_file(filename=""):
    """Reads a text file
    """
    with open(filename, encoding="utf-8") as f:
        readfile = f.read()
        print(readfile, end="")


