#!/usr/bin/env python3
"""
A module that takes an integer max_delay
and returns asyncio.Task
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Takes an integer and returns asyncio.Task
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
