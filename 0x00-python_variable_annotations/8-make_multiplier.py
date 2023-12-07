#!/usr/bin/env python3
"""
A module that returns a function that multiplies a float
by multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Takes a float multiplier as arg and returns
    a function that multiplies a float by multiplier
    """
    def square(a: float) -> float:
        """
        Finds the square of numbers
        """
        return float(a * multiplier)
    return square
