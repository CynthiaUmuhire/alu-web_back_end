#!/usr/bin/env python3

"""
define a function that takes in arguments with default values
"""
"""
define variables
"""
a = 1
pi = 3.14
i_understand_annotations = True
school = "Holberton"


def define_variables(a: int = 1, pi: float = 3.14,
                     i_understand_annotations: bool = "true",
                     school: str = "Holberton"):
    """
    return a string with the default values
    """
    a = a
    pi = pi
    i_understand_annotations = i_understand_annotations
    school = school
    return a, pi, i_understand_annotations, school


print(define_variables())
