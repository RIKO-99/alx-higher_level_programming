#!/usr/bin/python3

"""
    contains function reads a text file

"""

def read_file(filename=""):
    """
    reads a text file
    """
    with open(filename, encoding="utf-8") as f:
        readfile = f.read()
        print(readfile, end="")


