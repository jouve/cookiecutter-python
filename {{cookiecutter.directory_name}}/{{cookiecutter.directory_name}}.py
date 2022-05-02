import logging
from argparse import ArgumentParser


def add(aaa: int, bbb: int) -> int:
    return aaa + bbb


def main():
    parser = ArgumentParser()
    parser.add_argument('-V', '--version', version='0.1.0')
    parser.add_argument('-v', '--verbose', action='count', default=0)
    args = parser.parse_args()

    logging.basicConfig(level=[logging.WARNING, logging.INFO, logging.DEBUG][min(args.verbose, 2)])

    return 0
