#!/usr/bin/python
import logging
import argparse
import json

from teams import team_stats

TEAM_ROSTER_ACTION = "roster"


def _configure_logger():
    # Configure logging
    logger = logging.getLogger('pynba')
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler('../pynba.log')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)


def _configure_arg_parser():
    parser.add_argument("action", help="The action to perform", type=str)
    parser.add_argument("name", help="The name of the team or player", type=str)


if __name__ == "__main__":
    _configure_logger()

    cli_logger = logging.getLogger('pynba.cli')
    cli_logger.info("Welcome to pynba")

    parser = argparse.ArgumentParser()
    _configure_arg_parser()
    args = parser.parse_args()

    if args.action == TEAM_ROSTER_ACTION:
        name = args.name
        cli_logger.info('{} action called on {}'.format(TEAM_ROSTER_ACTION, name))
        response = team_stats.get_team_roster(name)
        print(json.dumps(response, indent=4, sort_keys=True))

