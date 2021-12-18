from Game import Direction


class Wolf:
    x = 0.0
    y = 0.0
    wolf_move_dist = 0.0

    def __init__(self, wolf_move_dist):
        self.wolf_move_dist = wolf_move_dist

    def move(self, direction):
        match direction:
            case Direction.NORTH:
                self.y += self.wolf_move_dist
            case Direction.EAST:
                self.x += self.wolf_move_dist
            case Direction.SOUTH:
                self.y -= self.wolf_move_dist
            case Direction.WEST:
                self.x -= self.wolf_move_dist

    def eat(self, sheep):
        self.x = sheep.x
        self.y = sheep.y
        sheep = None
