#!/usr/bin/env python3
"""
import the List and Union classes from the typing module

"""
from typing import List, Union
"""
Function that takes in a list of integers
 and floats and returns the sum as a float
"""


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    return the sum of the list
    """
    return sum(mxd_lst)
