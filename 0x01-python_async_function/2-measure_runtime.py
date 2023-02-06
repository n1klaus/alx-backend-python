#!/usr/bin/env python3
"""Measuring the runtime of a Asynchronous coroutine"""

import asyncio
import random
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    """Returns a float of the total execution time"""
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_elapsed = time.perf_counter() - start
    return total_elapsed / n
