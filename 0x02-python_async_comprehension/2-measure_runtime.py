#!/usr/bin/env python3
"""
A module that implements measure_runtime() coroutine
"""
import asyncio
import time
from typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    A coroutine that measure runtime for executing
    async_comprehension()
    """
    start_time = time.time()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    end_time = time.time()
    total_runtime = end_time - start_time

    return total_runtime
