import argparse
from highscoringwords import HighScoringWords
import time
import logging


def solution(is_letters, input_file, output_file):
    src_mod = HighScoringWords()
    if is_letters:
        with open(input_file, 'r') as f:
            string = f.read().splitlines()
        output_list = src_mod.build_leaderboard_for_letters(string[0])
    else:
        output_list = src_mod.build_leaderboard_for_word_list()

    with open(output_file, 'w') as f:
        for word in output_list:
            f.write("%s\n" % word)
    return output_list


def argparse_main():
    """
    parses the command line arguments and options, and performs operations
    """

    parser = argparse.ArgumentParser(description='Run Scrabble Leaderboard in Python')

    parser.add_argument('-l', '--letters',
                        action=argparse.BooleanOptionalAction,
                        help="Building leaderboard using letters",
                        dest="is_letters",
                        type=bool)
    parser.add_argument('-i', '--input',
                        action='store',
                        help="Text file containing alphabets for Scrabble game",
                        dest="input_file",
                        default='files/input.txt')
    parser.add_argument('-o', '--output',
                        action='store',
                        help="Text file containing STDOUT for Scrabble game",
                        dest="output_file",
                        default='files/output.txt')
    parser.add_argument('-d', '--debug',
                        help="Log DEBUG level output",
                        action="store_const", dest="loglevel", const=logging.DEBUG,
                        default=logging.WARNING,
                        )
    parser.add_argument('-v', '--verbose',
                        help="Log INFO level output",
                        action="store_const", dest="loglevel", const=logging.INFO,
                        )
    logging.basicConfig(format="%(asctime)s %(levelname)s:%(name)s: %(message)s",
                        level=parser.parse_args().loglevel,
                        datefmt="%H:%M:%S",
                        )

    args = parser.parse_args()
    start = time.perf_counter()
    output = solution(is_letters=args.is_letters, input_file=args.input_file, output_file=args.output_file)
    end = time.perf_counter()
    nl = '\n'
    print(f'The top {len(output)} words on the leaderboard are {nl}{nl.join(output)} \nand the leaderboard is '
          f'generated in {end - start:.4f} seconds')


if __name__ == "__main__":
    argparse_main()
