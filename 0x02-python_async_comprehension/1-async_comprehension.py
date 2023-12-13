#!/usr/bin/env python3
"""
A module that implements the async_comprehension
"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    A coroutine that collects random nums using async_gen()
    """
    result = []
    async for num in async_generator():
        result.append(num)
    return result
