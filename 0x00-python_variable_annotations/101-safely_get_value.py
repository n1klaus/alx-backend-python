#!/usr/bin/env python3
"""Basic annotations on Typevar"""


from typing import Mapping, TypeVar, Any, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """Return the value in a dictionary from key or the default"""
    if key in dct:
        return dct[key]
    else:
        return default
