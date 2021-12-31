import argparse
from Game import Game

if __name__ == '__main__':
    # rounds, sheeps, sheep_move_dist, wolf_move_dist, sheep_init_pos, wait, directory
    game = Game(50, 15, 0.5, 1.0, 10, False, "./")
    game.play()

    parser = argparse.ArgumentParser(description='Wolf and sheeps simulator')
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
                        help='Number of sheeps in the game. Default: 15',
                        type=int,
                        default=15,
                        metavar="NUM")
    parser.add_argument('-w', '--wait',
                        action='store_true',
                        help='Wait for user action after the end of every round. Default: false',
                        default=False)

    args = parser.parse_args()
    print("Args: ", args)

# -c/--config FILE - dodatkowy plik konfiguracyjny, gdzie FILE - nazwa pliku;
# -d/--dir DIR - podkatalog, w którym mają zostać zapisane pliki pos.json, alive.csv oraz - opcjonalnie - chase.log, gdzie DIR - nazwa podkatalogu;
# -h/--help - pomoc;
# -l/--log LEVEL - zapis zdarzeń do dziennika, gdzie LEVEL - poziom zdarzeń (DEBUG, INFO, WARNING, ERROR lub CRITICAL);
# -r/--rounds NUM - liczba tur, gdzie NUM - liczba całkowita;
# -s/--sheep NUM - liczba owiec, gdzie NUM - liczba całkowita;
# -w/--wait - oczekiwanie na naciśnięcie klawisza po wyświetlaniu podstawowych informacji o stanie symulacji na zakończenie każdej tury.
