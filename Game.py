import csv
import json
import math
import configparser
import logging

from pathlib import Path

# from Sheep import Sheep
from Direction import Direction
from Sheep import Sheep
from Wolf import Wolf


class ConfigError(Exception):
    pass

# SPELNIONE WYMAGANIA Z WIKAMPA NA 3:
# 0. WYMAGANIA FORMALNE DOPASOWAC
# 1. gotowe
# 2. gotowe, sprawdzic czy dobrze
# 3. gotowe
# 4. gotowe

# WYMAGANIA NA 4:
# 1. zrobione :)
# 2. argumenty wywołania (argparse) - not done
#       dir - done
#       wait - done
#       log - done
#       config - done
#       game_params - done
# 3. plik konfiguracyjny (configparser) - done
# 4. logowanie do chase.log (logging from std) - dun


class Game:
    def __init__(self, rounds, sheep, wait, directory, config_file):
        logging.debug(
            f"Game has been initialized with args: "
            f"rounds: {rounds}, sheep: {sheep}, wait: {wait}, directory: {directory}, config_file: {config_file}")
        # params
        self.rounds = rounds
        self.no_of_sheep = sheep
        self.sheep_move_dist = 0.5
        self.wolf_move_dist = 1.0
        self.init_pos_limit = 10

        self.wait = wait
        self.directory = directory + "/"

        if config_file:
            self.read_config_file(config_file)

        self.wolf = Wolf(self.wolf_move_dist)
        self.sheep_list = []
        for i in range(self.no_of_sheep):
            self.sheep_list.append(
                Sheep(self.sheep_move_dist, self.init_pos_limit, i)
            )

    def read_config_file(self, config_file):
        logging.debug(f"executed with args: config_file: {config_file}")
        config = configparser.ConfigParser()
        config.read(config_file)

        try:
            self.init_pos_limit = config.getfloat('Terrain', 'InitPosLimit')
            self.sheep_move_dist = config.getfloat('Movement', 'SheepMoveDist')
            self.wolf_move_dist = config.getfloat('Movement', 'WolfMoveDist')

            if self.init_pos_limit <= 0:
                raise ValueError('InitPosLimit must be greater than 0')
            if self.sheep_move_dist <= 0:
                raise ValueError('SheepMoveDist must be greater than 0')
            if self.wolf_move_dist <= 0:
                raise ValueError('WolfMoveDist must be greater than 0')
        except configparser.NoOptionError as e:
            raise ConfigError('Wrong config file structure: ' + str(e))
        except ValueError as e:
            raise ConfigError('Invalid data in config file: ' + str(e))

    def play(self):
        logging.debug("executed")
        csv_data = []
        json_data = []
        for i in range(self.rounds):
            logging.info(f"round {i} has started")
            eaten = None
            if not self.sheep_list:
                return
            for sheep in self.sheep_list:
                sheep.move()
            chased = False
            (nearest, dist) = self.get_nearest_sheep()
            if dist < self.wolf_move_dist:
                self.sheep_list.remove(nearest)
                self.wolf.eat(nearest)
                eaten = nearest
            else:
                # TODO: refactor move to accept vector as direction and move wolf in direction to nearest sheep
                self.wolf.move(self.calc_direction(nearest))
                chased = True
            json_data.append(self.get_pos_data(i))
            csv_data.append([i, len(self.sheep_list)])
            self.print_round(i, nearest.number, chased, eaten)

            if self.wait:
                input("Press Enter to go to the next round...")
        self.save_data(csv_data, json_data)

    def calc_direction(self, sheep):
        logging.debug(f"executed with args: sheep: {sheep.number}")
        diff_x = self.wolf.x - sheep.x
        diff_y = self.wolf.y - sheep.y
        if math.fabs(diff_x) > math.fabs(diff_y):
            if diff_x > 0:
                direction = Direction.WEST
            else:
                direction = Direction.EAST
        else:
            if diff_y > 0:
                direction = Direction.SOUTH
            else:
                direction = Direction.NORTH
        logging.debug(f"returned value direction: {direction}")
        return direction

    def get_pos_data(self, round_number):
        logging.debug(f"executed with args: round_number: {round_number}")
        sheep_pos = []
        # TODO check if it is possible to do it better
        for s in self.sheep_list:
            sheep_pos.append([s.x, s.y])

        pos_data = {"round_no": round_number, "wolf_pos": (self.wolf.x, self.wolf.y), "sheep_pos": sheep_pos}
        logging.debug(f"returned value pos_data: {pos_data}")
        return pos_data

    def calc_distance(self, sheep):
        logging.debug(f"executed with args: sheep: {sheep.number}")
        dist = math.sqrt((sheep.x - self.wolf.x) ** 2 + (sheep.y - self.wolf.y) ** 2)
        logging.debug(f"returned value dist: {dist}")
        return dist

    def get_nearest_sheep(self):
        # returns tuple made from the nearest sheep and its distance from wolf
        logging.debug("executed")
        res = (
            self.sheep_list[0],
            self.calc_distance(self.sheep_list[0])
        )
        for sheep in self.sheep_list:
            dist = self.calc_distance(sheep)
            if dist < res[1]:
                res = (sheep, dist)
        logging.debug(f"returned tuple res: {res}")
        return res

    def print_round(self, round_number, chased_sheep, chased, eaten):
        logging.debug(f"executed with args: "
                      f"round_number: {round_number}, chased_sheep: {chased_sheep}, "
                      f"chased: {chased}, eaten: {eaten.number if eaten else None}")
        print({
                "round": round_number,
                "wolf_pos": (self.wolf.x, self.wolf.y),
                "sheep": len(self.sheep_list),
                "chased_sheep": chased_sheep if chased else "None",
                "eaten_sheep": eaten.number if eaten else "None"
            })

    def save_data(self, csv_data, json_data):
        logging.debug(f"executed with args: csv_data: {csv_data}, json_data: {json_data}")
        Path(self.directory).mkdir(parents=True, exist_ok=True)

        with open(self.directory + "alive.csv", "w", newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(csv_data)

        with open(self.directory + "pos.json", 'w') as json_file:
            json.dump(json_data, json_file, indent=3)
