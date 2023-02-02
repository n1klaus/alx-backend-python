#!/usr/bin/env python3
"""Basic annotations on complex types - string and int/float in function"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple of key string and square float value"""
    return (k, float(v ** 2))
