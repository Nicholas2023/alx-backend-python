#!/usr/bin/env python3
"""
A module that returns the params of a functions
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns the params of a functions
    """
    return [(i, len(i)) for i in lst]
