#!/usr/bin/python3
"""Prints all public names defined in hidden_4.pyc, sorted alphabetically"""
import hidden_4

if __name__ == "__main__":
    names = [name for name in dir(hidden_4) if not name.startswith("__")]
    for name in sorted(names):
        print(name)
