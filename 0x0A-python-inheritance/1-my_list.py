#!/usr/bin/python3
"""
    This is my class Mylist that inherits from list
"""

class Mylist(list):
    def __init__(self):
        super().__init__()

    def print_sorted(self):
    """
    prints the sorted list

    """
    print(sorted(self))

