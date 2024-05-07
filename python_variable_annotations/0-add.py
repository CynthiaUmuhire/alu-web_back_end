#!/usr/bin/env python3

"""
define a type annotated function that adds two float
numbers and return the sum as a float
"""


def add(a: float, b: float) -> float:
    """
    Add two float numbers and return the sum as a float
    """
    return a + b


if __name__ == "__main__":
    print(add(10.5, 20.5))  # 31.0
    print(add(10.0, 20))  # 30.0
