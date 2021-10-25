import math
from enum import Enum

from Sheep import Sheep
from Wolf import Wolf


class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


def play():
    # constraints
    sheep_list = []
    sheep_move_dist = 0.1
    wolf_move_dist = 0.1
    sheep_init_pos = 1.2

    # initialization
    wolf = Wolf(wolf_move_dist)
    for i in range(50):
        s = Sheep(sheep_move_dist, sheep_init_pos)
        sheep_list.append(s)

    # game
    rounds = 50
    for i in range(rounds):
        for sheep in sheep_list:
            sheep.move()


def calc_distance(sheep, wolf):
    return math.sqrt((sheep.x - wolf.x) ** 2 + (sheep.y - wolf.y) ** 2)


def get_nearest_sheep(wolf, sheep_list):
    # returns tuple made from nearest sheep and its distance from wolf
    res = (sheep_list[0], calc_distance(sheep_list[0], wolf))
    for sheep in sheep_list:
        dist = calc_distance(sheep, wolf)
        if dist < res[1]:
            res = (sheep, dist)
    return res
