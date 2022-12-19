#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        Ans = a / b
    except ZeroDivisionError:
        Ans = None

    finally:
        print("Inside result: {}".format(Ans))
    return Ans
