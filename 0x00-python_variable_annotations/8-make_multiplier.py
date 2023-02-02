#!/usr/bin/env python3
"""Basic annotations on complex types - functions"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by argument"""
    def multiply(m: float) -> float:
        """Multiplies the argument with a float and returns the value"""
        return multiplier * m
    return multiply
