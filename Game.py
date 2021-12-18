import csv
import math

# from Sheep import Sheep
from Direction import Direction
from Sheep import Sheep
from Wolf import Wolf


# SPELNIONE WYMAGANIA Z WIKAMPA NA 3:
# 0. WYMAGANIA FORMALNE DOPASOWAC
# 1. gotowe
# 2. gotowe, sprawdzic czy dobrze
# 3. jest funkcja do pobrania tych danych, wystarczy zapisac do jsona
# 4. gotowe


def play():
    # constraints
    sheep_list = []
    rounds = 50
    no_of_sheep = 15
    sheep_move_dist = 0.5
    wolf_move_dist = 1.0
    sheep_init_pos = 10

    # initialization
    wolf = Wolf(wolf_move_dist)
    for i in range(no_of_sheep):
        s = Sheep(sheep_move_dist, sheep_init_pos, i)
        sheep_list.append(s)

    with open("alive.csv", "w", newline='') as file:
        writer = csv.writer(file)
        for i in range(rounds):
            eaten = None
            writer.writerow([i, len(sheep_list)])
            if not sheep_list:
                return
            for sheep in sheep_list:
                sheep.move()
            chased = False
            (nearest, dist) = get_nearest_sheep(wolf, sheep_list)
            if dist < wolf_move_dist:
                sheep_list.remove(nearest)
                wolf.eat(nearest)
                eaten = nearest
            else:
                # TODO: refactor move to accept vector as directin and move wolf in direction to nearest sheep
                wolf.move(calc_direction(wolf, nearest))
                chased = True
            res = {"round": i, "wolf_pos": (wolf.x, wolf.y), "sheeps": len(sheep_list),
                   "chased_sheep": nearest.number if chased else "None",
                   "eaten_sheep": eaten.number if eaten else "None"}
            print(res)


def calc_direction(wolf, sheep):
    diff_x = wolf.x - sheep.x
    diff_y = wolf.y - sheep.y
    dir = Direction.NORTH
    if math.fabs(diff_x) > math.fabs(diff_y):
        if diff_x > 0:
            dir = Direction.WEST
        else:
            dir = Direction.EAST
    else:
        if diff_y > 0:
            dir = Direction.SOUTH
        else:
            dir = Direction.NORTH
    return dir


def get_data(round, wolf, sheep):
    sheep_pos = []
    # TODO check if it is possible to do it better
    for s in sheep:
        sheep_pos.append([s.x, s.y])
    res = {"round_no": round, "wolf_pos": (wolf.x, wolf.y), "sheep_pos": sheep_pos}
    return res


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
