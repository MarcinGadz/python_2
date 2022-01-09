import logging
import math


class Wolf:
    x = 0.0
    y = 0.0
    wolf_move_dist = 0.0

    def __init__(self, wolf_move_dist):
        logging.debug(f"Wolf has been initialized with args: wolf_move_dist: {wolf_move_dist}")
        self.wolf_move_dist = wolf_move_dist

    def move(self, nearest_sheep):
        logging.debug(f"executed with args: nearest_sheep: {nearest_sheep.number}")
        (old_x, old_y) = (self.x, self.y)

        dist = math.sqrt((nearest_sheep.x - self.x) ** 2 + (nearest_sheep.y - self.y) ** 2)
        dx = (nearest_sheep.x - self.x) / dist
        dy = (nearest_sheep.y - self.y) / dist

        self.x += dx
        self.y += dy

        logging.info(f"wolf moved from [{old_x}, {old_y}] to [{self.x}, {self.y}] - vector is [{dx}; {dy}]")

    def eat(self, sheep):
        logging.debug(f"executed with args: sheep: {sheep.number}")
        self.x = sheep.x
        self.y = sheep.y
        sheep.lives = False
        logging.info(f"sheep {sheep.number} has been eaten. "
                     f"New wolf position: [{self.x}, {self.y}]")
