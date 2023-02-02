#!/usr/bin/env python3
"""Basic annotations on sequence"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns a sequence of elements or None depending on the argument"""
    if lst:
        return lst[0]
    else:
        return None
