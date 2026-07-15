#!/usr/bin/python3
"""Safe printing of an integer"""


def safe_print_integer(value):
    """Print an integer using {:d}.format(), returning True on success."""
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False
