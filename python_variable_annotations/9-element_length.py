#!/usr/bin/env python3
"""
importing the List and Tuple modules from the typing module
"""
from typing import List, Tuple
"""
function element_length that takes a list of strings lst as argument
and returns a list of tuples where each tuple contains a string and an
integer.
"""


def element_length(lst: List[int]) -> List[Tuple[int, int]]:
    """
    returns a list of tuples where each tuple contains a string and an
    integer.
    """
    return [(i, len(i)) for i in lst]
