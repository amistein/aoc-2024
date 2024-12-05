import re

from typing import Callable, TypeVar
T = TypeVar('T')

def count_pred(l: list[T], pred: Callable[[T], bool] = bool):
    return sum([1 if pred(item) else 0 for item in l])

def lines(s: str):
    return s.strip().splitlines()

def int_pair(s: str):
    l = [int(e) for e in s.split()]
    return (l[0], l[1])

def ints(text: str) -> list[int]:
    """A tuple of all the integers in text, ignoring non-number characters."""
    return list(map(int, re.findall(r'-?[0-9]+', text)))
