#!/usr/bin/env python3

"""
define a function that takes in arguments with default values
"""


def define_variables(a: int = 1, pi: float = 3.14,
                     i_understand_annotations: bool = "true",
                     school: str = "Holberton") -> str:
    """
    return a string with the default values
    """
    return {a}, {pi}, {i_understand_annotations}, {school}
