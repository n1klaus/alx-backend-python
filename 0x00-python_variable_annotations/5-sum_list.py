#!/usr/bin/env python3
"""Basic annotations on complex types in a function"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """Returns the sum of a list of floats"""
    sum: float = 0
    for num in input_list:
        sum += num
    return sum
