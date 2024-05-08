#!/usr/bin/env python3
"""
importing the Union module from the typing module
"""
from typing import Union
"""
function to_kv that takes a string k and an int OR float v as arguments and returns a tuple.
"""


def to_kv(k: str, v: Union[str, float]) -> tuple:
    """
    returns a tuple containing k and the square of v.
    """
    return (k, v**2)
