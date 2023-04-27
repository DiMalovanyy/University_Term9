import pygame

from object.player import Player
from object.wall import Wall
from pacman.types import Direction


class GameRenderer:
    def __init__(self, in_width: int, in_height: int):
        pygame.init()
        self._width = in_width
        self._height = in_height
        self._screen = pygame.display.set_mode((in_width, in_height))
        pygame.display.set_caption('Pacman')
        self._clock = pygame.time.Clock()
        self._done = False
        self._game_objects = []
        self._walls = []
        self._ghosts = []
        self._cookies = []
        self._hero: Player | None =  None

    def tick(self, in_fps: int):
        black = (0, 0, 0)
        while not self._done:
            for game_object in self._game_objects:
                game_object.tick()
                game_object.draw()

            pygame.display.flip()
            self._clock.tick(in_fps)
            self._screen.fill(black)
            self._handle_events()
        print("Game over")

    def add_game_object(self, obj):
        self._game_objects.append(obj)

    def add_cookie(self, obj):
        self._game_objects.append(obj)
        self._cookies.append(obj)

    def add_wall(self, obj: Wall):
        self.add_game_object(obj)
        self._walls.append(obj)

    def add_ghost(self, ghost):
        self.add_game_object(ghost)
        self._ghosts.append(ghost)

    def get_ghosts(self):
        return self._ghosts

    def get_walls(self):
        return self._walls

    def get_cookies(self):
        return self._cookies

    def get_game_objects(self):
        return self._game_objects

    def add_hero(self, in_hero):
        self.add_game_object(in_hero)
        self._hero = in_hero

    def get_hero(self):
        return self._hero

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._done = True

        pressed = pygame.key.get_pressed()
        if self._hero is not None:
            if pressed[pygame.K_UP]:
                self._hero.set_direction(Direction.UP)
            elif pressed[pygame.K_LEFT]:
                self._hero.set_direction(Direction.LEFT)
            elif pressed[pygame.K_DOWN]:
                self._hero.set_direction(Direction.DOWN)
            elif pressed[pygame.K_RIGHT]:
                self._hero.set_direction(Direction.RIGHT)
