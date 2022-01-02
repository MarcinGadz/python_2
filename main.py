import argparse
import configparser
import logging
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

    if args.log:
        level = logging.getLevelName(args.log)
        logging.basicConfig(level=level, filename='chase.log', filemode='w', force=True,
                            format='%(asctime)s [%(filename)12s:%(lineno)3s - %(funcName)20s()]: %(levelname)s: %(message)s')

    try:
        game = Game(args.rounds, args.sheep, args.wait, args.dir, args.config)
    except ConfigError as e:
        logging.error("Exception has been caught: " + str(e))
        sys.exit(e)

    game.play()
