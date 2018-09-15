#!/usr/bin/python
import logging
import argparse
import json

from teams import team_stats, TeamNotFoundException
from visual import tables


TEAM_ROSTER_ACTION = "roster"


def _configure_logger():
    """
    Define the logging parameters
    """
    # Configure logging
    logger = logging.getLogger('pynba')
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler('../pynba.log')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)


def _configure_arg_parser():
    """
    Configures the arguments
    """
    parser.add_argument("action", help="The action to perform", type=str)
    parser.add_argument("name", help="The name of the team or player", type=str)


def _get_team_roster(team_name_input):
    """
    calls the team module and returns the team roster.
    :param team_name_input: team name as from input
    :return: json string for the team roster
    """
    logger = logging.getLogger('pynba.main')

    try:
        logger.info('{action_name} action called on {name}'.format(action_name=TEAM_ROSTER_ACTION, name=team_name_input))
        response_string = team_stats.get_team_roster(team_name_input)
    except TeamNotFoundException:
        error_message = 'No team found for the given name {name}. ' \
                        'Use either the city name, franchise name or the 3 digit code'\
                        .format(name=team_name_input)
        logger.error(error_message)
        response_string = error_message

    return response_string


if __name__ == "__main__":
    _configure_logger()

    parser = argparse.ArgumentParser()
    _configure_arg_parser()
    args = parser.parse_args()

    # Do action as per the argument
    if args.action == TEAM_ROSTER_ACTION:
        name = args.name
        response = _get_team_roster(name)
        if response:
            #print(json.dumps(response, indent=4, sort_keys=True))
            print(tables.build_tables_from_json(["PLAYER", "POSITION", "HEIGHT", "WEIGHT"], list(response)))

