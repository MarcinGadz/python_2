import random

from Game import Direction


class Sheep:
    x = 0.0
    y = 0.0
    number = 0
    move_dist = 0.0

    # Constructor
    def __init__(self, move_dist, init_pos_limit, number):
        self.move_dist = move_dist
        self.generate_init_pos(init_pos_limit)
        self.number = number

    def generate_init_pos(self, init_pos_limit):
        self.x = random.uniform(-init_pos_limit, init_pos_limit)
        self.y = random.uniform(-init_pos_limit, init_pos_limit)

    def move(self):
        direction = random.randint(0, 3)
        match direction:
            case Direction.NORTH:
                self.y += self.move_dist
            case Direction.EAST:
                self.x += self.move_dist
            case Direction.SOUTH:
                self.y -= self.move_dist
            case Direction.WEST:
                self.x -= self.move_dist
