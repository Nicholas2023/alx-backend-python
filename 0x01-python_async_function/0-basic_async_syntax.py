#!/usr/bin/env python3
"""
A module that implements an asynchronous coroutine
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Async coroutine that takes an integer (0 - 10) sec
    and eventually returns it
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
