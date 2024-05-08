#!/usr/bin/env python3
from typing import List

"""
a function that gets a list of floats and returns their sum as a float
"""


def sum_list(input_list: List[float]) -> float:
    """
    return the sum of the list
    """
    return sum(input_list)


print(sum_list([1.0, 2.0, 3.0]))  # 6.0
