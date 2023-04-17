#!/usr/bin/env python3
"""Running an asyncio Task"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """Runs the asyncio task"""
    coroutines = [task_wait_random(max_delay) for _ in range(n)]
    return [await coroutine for coroutine in asyncio.as_completed(coroutines)]
