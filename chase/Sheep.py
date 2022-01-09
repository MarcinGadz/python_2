import random
import logging

from chase.Game import Direction


class Sheep:
    x = 0.0
    y = 0.0
    number = 0
    move_dist = 0.0

    # Constructor
    def __init__(self, move_dist, init_pos_limit, number):
        logging.debug(f"Sheep has been initialized with args: "
                      f"move_dist: {move_dist}, init_pos_limit: {init_pos_limit}, number: {number}")
        self.move_dist = move_dist
        self.generate_init_pos(init_pos_limit)
        self.number = number
        self.lives = True

    def generate_init_pos(self, init_pos_limit):
        logging.debug(f"executed with args: init_pos_limit: {init_pos_limit}")
        self.x = random.uniform(-init_pos_limit, init_pos_limit)
        self.y = random.uniform(-init_pos_limit, init_pos_limit)
        logging.info(f"sheep pos has been generated: [{self.x}, {self.y}]")

    def move(self):
        logging.debug(f"executed")
        direction = random.randint(0, 3)
        (old_x, old_y) = (self.x, self.y)
        match direction:
            case Direction.NORTH:
                self.y += self.move_dist
            case Direction.EAST:
                self.x += self.move_dist
            case Direction.SOUTH:
                self.y -= self.move_dist
            case Direction.WEST:
                self.x -= self.move_dist
        logging.info(f"sheep moved from [{old_x}, {old_y}] to [{self.x}, {self.y}]")
