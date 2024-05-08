#!/usr/bin/env python3
"""
importing the List and Tuple modules from the typing module
"""
from typing import List, Tuple, Iterable
"""
function element_length that takes a list of strings an iterable
and returns a list of tuples where each tuple contains a string and an
integer.
"""


def element_length(lst: Iterable) -> List[Tuple[int, int]]:
    """
    returns a list of tuples where each tuple contains a string and an
    integer.
    """
    return [(i, len(i)) for i in lst]
