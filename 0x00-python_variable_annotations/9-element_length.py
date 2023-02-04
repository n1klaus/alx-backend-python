#!/usr/bin/env python3
"""Basic annotations on function's parameters"""

from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return tuple of item and its length from an iterable"""
    return [(i, len(i)) for i in lst]
