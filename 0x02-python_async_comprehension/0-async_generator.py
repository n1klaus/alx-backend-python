#!/usr/bin/env python3
"""Async generator"""


import asyncio
import random
from typing import Iterable


async def async_generator() -> Iterable[float]:
    """Yields a random float between 0 and 10"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
