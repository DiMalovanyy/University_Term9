from abc import ABC
import tcod
import numpy as np

class Pathfinder:
    def get_path(self, from_x, from_y, to_x, to_y):
        pass

class AStarPathfinder(Pathfinder):
    def __init__(self, in_arr):
        cost = np.array(in_arr, dtype=np.bool_).tolist()
        self.pf = tcod.path.AStar(cost=cost, diagonal=0)

    def get_path(self, from_x, from_y, to_x, to_y) -> list:
        res = self.pf.get_path(from_x, from_y, to_x, to_y)
        return [(sub[1], sub[0]) for sub in res]

class DjksrtaPathfinder(Pathfinder):
    def __init__(self, in_arr):
        cost = np.array(in_arr, dtype=np.bool_).tolist()
        self.pf = tcod.path.Dijkstra(cost=cost, diagonal=0)

    def get_path(self, from_x, from_y, to_x, to_y) -> list:
        self.pf.set_goal(from_x, from_y)
        res = self.pf.get_path(to_x, to_y)
        return [(sub[1], sub[0]) for sub in res]
        
    


