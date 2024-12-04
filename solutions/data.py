from typing import Callable, TypeVar
T = TypeVar('T')

# Source: https://github.com/norvig/pytudes/blob/main/ipynb/Advent-2020.ipynb
def get_data(day: int, parser: Callable[[str], T] = str, sep: str = '\n'):
    "Split the day's input file into sections separated by `sep`, and apply `parser` to each."
    with open(f'input/day_{day}.txt') as f:
        sections = f.read().rstrip().split(sep)
        return list(map(parser, sections))
