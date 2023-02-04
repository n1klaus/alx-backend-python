#!/usr/bin/env python3
"""Type checking with mypy"""

from typing import Union, List, Tuple, Any
from typing_extensions import Protocol


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Returns a list of elements from the argument"""
    zoomed_in: List = [
        item for item in list(lst)
        for i in range(int(factor))
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(tuple(array))

zoom_3x = zoom_array(tuple(array), int(3.0))
