#!/usr/bin/env python3
"""Multiple Asynchronous coroutines at the same time using random delay"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """Returns a sorted list of floats after a random delay"""
    coroutines = [wait_random(max_delay) for _ in range(n)]
    return [await coroutine for coroutine in asyncio.as_completed(coroutines)]
