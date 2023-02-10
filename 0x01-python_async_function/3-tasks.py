#!/usr/bin/env python3
"""Creating an asyncio task"""

from asyncio import create_task, Task
import random
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 10) -> Task:
    """Returns the created asyncio.Task"""
    return create_task(wait_random(max_delay))
