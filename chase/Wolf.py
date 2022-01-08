import logging
from .Game import Direction


class Wolf:
    x = 0.0
    y = 0.0
    wolf_move_dist = 0.0

    def __init__(self, wolf_move_dist):
        logging.debug(f"Wolf has been initialized with args: wolf_move_dist: {wolf_move_dist}")
        self.wolf_move_dist = wolf_move_dist

    def move(self, direction):
        logging.debug(f"executed with args: direction: {direction}")
        (old_x, old_y) = (self.x, self.y)
        match direction:
            case Direction.NORTH:
                self.y += self.wolf_move_dist
            case Direction.EAST:
                self.x += self.wolf_move_dist
            case Direction.SOUTH:
                self.y -= self.wolf_move_dist
            case Direction.WEST:
                self.x -= self.wolf_move_dist
        logging.info(f"wolf moved from [{old_x}, {old_y}] to [{self.x}, {self.y}]")

    def eat(self, sheep):
        logging.debug(f"executed with args: sheep: {sheep.number}")
        self.x = sheep.x
        self.y = sheep.y
        logging.info(f"sheep {sheep.number} has been eaten. "
                     f"New wolf position: [{self.x}, {self.y}]")
        sheep = None
