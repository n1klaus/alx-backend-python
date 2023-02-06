#!/usr/bin/env python3
"""Multiple Asynchronous coroutines at the same time using random delay"""

import asyncio
import random
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> float:
    """Retuns an list of floats after a random delay"""
    return [await wait_random(max_delay) for _ in range(n)]
