from dataclasses import dataclass
from typing import NewType, Tuple, Generator
from enum import Enum

@dataclass
class Coords(tuple[float, float]):
    x: float
    y: float
    def __new__(cls, x, y):
        return tuple.__new__(Coords, (x, y))


Color = NewType("Color", Tuple[int, int, int])

class Direction(Enum):
    LEFT = 0
    UP = 1
    RIGHT = 2
    DOWN = 3,
    NONE = 4

