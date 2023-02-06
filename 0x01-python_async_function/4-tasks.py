#!/usr/bin/env python3
"""Running an asyncio Task"""

import asyncio
import random
task_wait_random = __import__('3-tasks').wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> float:
    """Runs the asyncio task"""
    return [await task_wait_random(max_delay) for _ in range(n)]
