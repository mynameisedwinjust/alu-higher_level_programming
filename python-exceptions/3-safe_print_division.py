#!/usr/bin/python3
"""Integers division with debug"""


def safe_print_division(a, b):
    """Divide a by b, printing the result inside finally."""
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
