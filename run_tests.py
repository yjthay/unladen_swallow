import os
import pathlib
import pytest
import coverage
import argparse


def argparse_test():
    parser = argparse.ArgumentParser(description='Control verbosity of pytest')

    parser.add_argument('-q', '--quiet',
                        help="Decrease verbosity",
                        action="store_const", dest="verbosity", const='-q',
                        default='-v', )

    parser.add_argument('-v', '--verbose',
                        help="Decrease verbosity",
                        action="store_const", dest="verbosity", const='-v',
                        default='-v')

    os.chdir(pathlib.Path.cwd() / 'test')

    cov = coverage.Coverage()
    cov.start()

    pytest.main([parser.parse_args().verbosity])

    cov.stop()
    cov.report()
    cov.html_report()


if __name__ == "__main__":
    argparse_test()
