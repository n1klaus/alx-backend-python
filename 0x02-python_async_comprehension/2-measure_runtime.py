#!/usr/bin/env python3
"""Run time for parallel comprehensions"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Returns the total measured runtime from 4 parallel executions of
    async comprehensions
    """
    start = time.perf_counter()
    await asyncio.gather(*[async_comprehension()] * 4)
    elapsed = time.perf_counter() - start
    return elapsed
