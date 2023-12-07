#!/usr/bin/env python3
"""
A module that returns the sum of mixed list types
"""
from typing import List, Union


def sum_mixed_list(mixed_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of mixed list
    """
    return sum(mixed_lst)
