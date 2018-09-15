#!/usr/bin/python
import logging
import argparse
import json

from teams import team_stats, TeamNotFoundException


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


def _get_team_roster(name):
    logger = logging.getLogger('pynba.main')
    try:
        logger.info('{action_name} action called on {name}'.format(action_name=TEAM_ROSTER_ACTION, name=name))
        response = team_stats.get_team_roster(name)
        return response
    except TeamNotFoundException:
        logger.error('No team found for the given name {name}. '
                     'Use either the city name, franchise name or the 3 digit code'
                     .format(name=name))

    return None


if __name__ == "__main__":
    _configure_logger()

    parser = argparse.ArgumentParser()
    _configure_arg_parser()
    args = parser.parse_args()

    if args.action == TEAM_ROSTER_ACTION:
        name = args.name
        response = _get_team_roster(name)
        if response:
            print(json.dumps(response, indent=4, sort_keys=True))

