from pathlib import Path
from pprint import pprint
from dataclasses import dataclass
from collections import namedtuple

from aocp import (
    IntParser, 
    ListParser, 
    IntListParser, 
    TupleParser, 
    BoolParser, 
    SortTransform, 
    SetParser,
)

from aocd.models import Puzzle


def get_raw_data(day: int) -> str:
    puzzle = Puzzle(year=2021, day=day)
    return puzzle.input_data

def print_head(string: str, limit: int = 10):
    for line in string.splitlines()[:limit]:
        print(line)

def print_start(string: str, limit: int = 50):
    print(string[:limit])




# raw_data = get_raw_data(4)
# print_head(raw_data, 20)
