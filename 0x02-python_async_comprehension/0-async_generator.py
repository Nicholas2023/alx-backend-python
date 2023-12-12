#!/usr/bin/env python3
"""
A module that implements the async_generator()
"""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    A coroutine that loops 10 times asynchronously
    then yield a random number between 0 and 10
    """
    for i in range(10):
        await asyncio.sleep(1)
        num = random.uniform(0, 10)
        yield num
