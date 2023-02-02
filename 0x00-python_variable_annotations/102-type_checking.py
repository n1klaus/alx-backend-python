#!/usr/bin/env python3
"""Type checking with mypy"""

from typing import Union, List, Optional, Any
from typing_extensions import Protocol


class NumRange(Protocol):
    value: Optional[Union[int, float]]


def zoom_array(lst: List[int], factor: Any = 2) -> List[List[int]]:
    """Returns a list of elements from the argument"""
    zoomed_in: List = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
