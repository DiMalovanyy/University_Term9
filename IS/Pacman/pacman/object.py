from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any

from .render import GameRenderer
from .types import Color, Coords

from pygame import Rect, Surface, draw

@dataclass
class GameObject(ABC):
    _size: int
    _game_renderer: GameRenderer
    _surface: Surface
    _coords: Coords 
    _color: Color
    _is_circle: bool
    _shape: Rect

    def draw(self) -> None:
        if self._is_circle: 
            draw.circle(self._surface, self._color, self._coords, self._size)
        else:
            rect_object = Rect(self._coords.x, self._coords.y, self._size, self._size)
            draw.rect(self._surface, self._color, rect_object, border_radius=4)

    @abstractmethod
    def tick(self) -> None: ...


    @property
    def shape(self) -> Rect:
        return self._shape

    @property 
    def position(self) -> Coords:
        return self._coords

    @position.setter
    def position(self, value: Coords) -> None:
        self._coords = value


class Wall(GameObject):
    def __init__(self):
        ...

