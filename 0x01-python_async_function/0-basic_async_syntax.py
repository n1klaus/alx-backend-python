#!/usr/bin/env python3
"""Asynchronous coroutine using random delay"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Retuns an integer argument after a random delay"""
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
