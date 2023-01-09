#!/usr/bin/python3
"""
    This is my class Mylist that inherits from list
"""
class list:
    """
    This is my super class list

    """
    def __init__(self):
        pass 

class Mylist(list):

    def print_sorted(self):
    """
    prints the sorted list

    """
    print(sorted(self))

