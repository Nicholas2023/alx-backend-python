#!/usr/bin/env python3
"""
A module that returns the list of all the delays(float values)
in ascending order
"""
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Returns the List of all delays (float values)
    in ascending order without using sort()
    """
    lst = []

    for i in range(n):
        delay = await wait_random(max_delay)
        lst.append(delay)

    return sorted(lst)
