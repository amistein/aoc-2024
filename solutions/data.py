from typing import Callable, TypeVar
T = TypeVar('T')

sections_func = Callable[[str], list[str]]

# Source: https://github.com/norvig/pytudes/blob/ecefbabb55992f259e7a7e6ffe05f1e75aaab8d6/ipynb/AdventUtils.ipynb
# with modifications

lines = str.splitlines # By default, split input text into lines
def paragraphs(text: str): return text.split('\n\n') # Split text into paragraphs
    
def get_data(day: int):
    "Split the day's input file into sections separated by `sep`, and apply `parser` to each."
    with open(f'input/day_{day}.txt') as f:
        return f.read().rstrip()
    
def parse(text: str, parser: Callable[[str], T] = str, sections: sections_func = lines):
    return list(map(parser, sections(text)))
