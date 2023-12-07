#!/usr/bin/env python3
"""
A module that returns a tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string and an int or float as args
    then returns a tuple
    """
    x = float(v * v)
    y = str(k)
    return (y, x)
