import pygame

from pacman.types import Direction
from .object import MovableObject

ghost_id = 0

class Ghost(MovableObject):
    def __init__(self, in_surface, x, y, in_size: int, in_game_controller, in_color=(255, 0, 0)):
        global ghost_id
        ghost_id += 1
        super().__init__(in_surface, x, y, in_size, in_color, False, id=ghost_id)
        self.game_controller = in_game_controller

    def reached_target(self):
        self.handle_player_catch()
        if (self.x, self.y) == self.next_target:
            self.next_target = self.get_next_location()
        self.current_direction = self.calculate_direction_to_next_target()


    def clear_path(self):
        self.location_queue.clear()

    def set_new_path(self, in_path):
        for item in in_path:
            self.location_queue.append(item)
        self.next_target = self.get_next_location()

    def calculate_direction_to_next_target(self) -> Direction:
        if self.next_target is None:
            self.game_controller.request_new_path(self, self._renderer.get_hero())
            return Direction.NONE
        diff_x = self.next_target[0] - self.x
        diff_y = self.next_target[1] - self.y
        if diff_x == 0:
            return Direction.DOWN if diff_y > 0 else Direction.UP
        if diff_y == 0:
            return Direction.LEFT if diff_x < 0 else Direction.RIGHT
        self.game_controller.request_new_path(self, self._renderer.get_hero())
        return Direction.DOWN

    def automatic_move(self, in_direction: Direction):
        if in_direction == Direction.UP:
            self.set_position(self.x, self.y - 1)
        elif in_direction == Direction.DOWN:
            self.set_position(self.x, self.y + 1)
        elif in_direction == Direction.LEFT:
            self.set_position(self.x - 1, self.y)
        elif in_direction == Direction.RIGHT:
            self.set_position(self.x + 1, self.y)

    def handle_player_catch(self):
        hero = self._renderer.get_hero()
        collision_rect = pygame.Rect(self.x, self.y, self._size, self._size)
        hero_position = pygame.Rect(hero.x, hero.y, hero._size, hero._size)

        if collision_rect.colliderect(hero_position):
            print("Catched")
            exit()
