#!/usr/bin/env python3

"""
define a function that takes a float in and return a string
"""


def to_str(n: float) -> str:
    """
    return the string representation of the number
    """
    return str(n)


if __name__ == "__main__":
    print(to_str(3.96))  # 3.96
    print(to_str(2.0))  # 2.0
    print(to_str(0.0))  # 0.0
    print(to_str(-4.2))  # -4.2
    print(to_str(-0.0))  # 0.0
