#!/usr/bin/python3
"""
Definition of a function lookup
"""

def lookup(obj):
    """Return a list of attributes and methods of an object
    
    obj(any): objects whosse attributes and methods are to be returned

    """
    return (dir(obj))
