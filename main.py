import argparse
import configparser
import sys

from Game import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Wolf and sheep simulator')
    parser.add_argument('--config',
                        help='Config file with input data')
    parser.add_argument('-d', '--dir',
                        help='Allows to save data to specified directory. Default: current folder',
                        default="./",
                        metavar="DIR")
    parser.add_argument('-l', '--log',
                        help='Allows to log events to specified file',
                        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
                        metavar="LEVEL")
    parser.add_argument('-r', '--rounds',
                        help='Number of rounds of the game. Default: 50',
                        type=int,
                        default=50,
                        metavar="NUM")
    parser.add_argument('-s', '--sheep',
                        help='Number of sheep in the game. Default: 15',
                        type=int,
                        default=15,
                        metavar="NUM")
    parser.add_argument('-w', '--wait',
                        action='store_true',
                        help='Wait for user action after the end of every round. Default: false',
                        default=False)

    args = parser.parse_args()
    print("Args: ", args)

    try:
        game = Game(args.rounds, args.sheep, args.wait, args.dir, args.config)
    except ConfigError as e:
        sys.exit(e)

    game.play()
