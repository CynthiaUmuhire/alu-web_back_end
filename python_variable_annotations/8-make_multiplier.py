#!/usr/bin/env python3
"""
importing the Callable module from the typing module
"""
from typing import Callable
"""
a function that takes a float multiplier as argument
and returns a function
"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    a function that takes a float multiplier as argument
    """
    def multiply(num: float) -> float:
        """
        returns the product of num and multiplier
        """
        return num * multiplier
    """
    returns the product of num and multiplier
    """
    return multiply
