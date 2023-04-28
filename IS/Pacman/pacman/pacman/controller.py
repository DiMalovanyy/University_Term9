
from object.wall import Wall
from object.ghost import Ghost
from object.player import Player
from object.point import Cookie

from .utils import translate_screen_to_maze, translate_maze_to_screen
from algorithm.pathfinder import AStarPathfinder, DjksrtaPathfinder

class PacmanGameController:
    def __init__(self):
        self.ascii_maze = [
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "X            XX     P      X",
            "X XXXX XXXXX XX XXXXX XXXX X",
            "X XXXX XXXXX XX XXXXX XXXX X",
            "X XXXX XXXXX XX XXXXX XXXX X",
            "X                          X",
            "X XXXX XX XXXXXXXX XX XXXX X",
            "X XXXX XX XXXXXXXX XX XXXX X",
            "X      XX    XX    XX      X",
            "XXXXXX XXXXX XX XXXXX XXXXXX",
            "XXXXXX XXXXX XX XXXXX XXXXXX",
            "XXXXXX XX          XX XXXXXX",
            "XXXXXX XX XXX  XXX XX XXXXXX",
            "XXXXXX XX XXX  XXX XX XXXXXX",
            "                       G    ",
            "XXXXXX XX XXX  XXX XX XXXXXX",
            "XXXXXX XX XXX  XXX XX XXXXXX",
            "XXXXXX XX          XX XXXXXX",
            "XXXXXX XX XXXXXXXX XX XXXXXX",
            "XXXXXX XX XXXXXXXX XX XXXXXX",
            "X            XX            X",
            "X XXXX XXXXX XX XXXXX XXXX X",
            "X XXXX XXXXX XX XXXXX XXXX X",
            "X   XX  G             XX   X",
            "XXX XX XX XXXXXXXX XX XX XXX",
            "XXX XX XX XXXXXXXX XX XX XXX",
            "X      XX    XX    XX      X",
            "X XXXXXXXXXX XX XXXXXXXXXX X",
            "X XXXXXXXXXX XX XXXXXXXXXX X",
            "X                          X",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        ]

        self.numpy_maze = []
        self.cookie_spaces = []
        self.reachable_spaces = []
        self.ghost_spawns = []
        self.ghost_colors = [
            (255, 184, 255),
            (255, 0, 20), # Rose
            (255, 184, 255),
            (255, 0, 20), #
        ]
        self.size = (0, 0)
        self.convert_maze_to_numpy()
        self.p = AStarPathfinder(self.numpy_maze)

    def request_new_path(self, in_ghost: Ghost, in_player):
        current_maze_coord = translate_screen_to_maze(in_ghost.get_position())
        current_player_position = translate_screen_to_maze(in_player.get_position()) 

        pathfinder = None
        if in_ghost.get_id() % 2 == 0:
            # Red
            pathfinder = AStarPathfinder(self.numpy_maze)
        else:
            # Rose
            pathfinder = DjksrtaPathfinder(self.numpy_maze)
            print("aa")
            
        path = pathfinder.get_path(current_maze_coord[1], current_maze_coord[0], current_player_position[1],
                               current_player_position[0])
        test_path = [translate_maze_to_screen(item) for item in path]
        in_ghost.clear_path()
        in_ghost.set_new_path(test_path)

    def rebuild_ghosts_path(self, ghosts, in_player):
        current_player_position = translate_screen_to_maze(in_player.get_position()) 
        for in_ghost in ghosts:
            current_maze_coord = translate_maze_to_screen(in_ghost.get_position())
            pathfinder = None
            
            if in_ghost.get_id() % 2 == 0:
                # Red
                pathfinder = AStarPathfinder(self.numpy_maze)
            else:
                # Rose
                pathfinder = DjksrtaPathfinder(self.numpy_maze)
                
            path = pathfinder.get_path(current_maze_coord[1], current_maze_coord[0], current_player_position[1],
                                   current_player_position[0])
            test_path = [translate_maze_to_screen(item) for item in path]
            in_ghost.clear_path()
            in_ghost.set_new_path(test_path) 

    def convert_maze_to_numpy(self):
        for x, row in enumerate(self.ascii_maze):
            self.size = (len(row), x + 1)
            binary_row = []
            for y, column in enumerate(row):
                if column == "G":
                    self.ghost_spawns.append((y, x))

                if column == "X":
                    binary_row.append(0)
                else:
                    binary_row.append(1)
                    self.cookie_spaces.append((y, x))
                    self.reachable_spaces.append((y, x))
            self.numpy_maze.append(binary_row)
