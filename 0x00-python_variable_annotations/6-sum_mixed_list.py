#!/usr/bin/env python3
"""Basic annotations on complex types - mixed lists in function"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum of a list of integers and floats"""
    sum: float = 0
    for num in mxd_lst:
        sum += num
    return sum
