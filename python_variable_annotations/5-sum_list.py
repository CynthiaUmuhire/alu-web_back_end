#!/usr/bin/env python3
"""
import the List module from the typing library
"""
from typing import List

"""
a function that gets a list of floats and returns their sum as a float
"""


def sum_list(input_list: List[float]) -> float:
    """
    return the sum of the list
    """
    return sum(input_list)


if __name__ == "__main__":
    print(sum_list([1.0, 2.0, 3.0]))  # 6.0
