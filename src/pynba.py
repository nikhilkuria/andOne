#!/usr/bin/python
import logging
import argparse
import json

from teams import team_stats, TeamNotFoundException
from players import player_stats, PlayerNotFoundException
from visual import tables, StackedGraph
from constants import TEAM_HEADERS, actions


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


def _show_results(result_string):
    """
    From the result string, present the result to the user
    A simple print statement for now
    :param result_string:
    """
    print(result_string)


def _get_team_roster(team_name_input):
    """
    calls the team module and returns the team roster.
    :param team_name_input: team name as from input
    :return: json string for the team roster
    """
    logger = logging.getLogger('pynba.main')

    try:
        logger.info('{action_name} action called on {name}'
                    .format(action_name=actions.TEAM_ROSTER_ACTION,
                            name=team_name_input))
        response_string = team_stats.get_team_roster(team_name_input)
    except TeamNotFoundException:
        error_message = 'No team found for the given name {name}. ' \
                        'Use either the city name, franchise name or the 3 digit code'\
                        .format(name=team_name_input)
        logger.error(error_message)
        response_string = error_message

    return response_string


def _get_player_stats(first_name, last_name):
    logger = logging.getLogger('pynba.main')

    try:
        logger.info('{action_name} action called on first_name = {first_name} and last_name = {last_name}'
                    .format(action_name=actions.PLAYER_SUMMARY_ACTION,
                            first_name=first_name,
                            last_name=last_name))
        player_stats_response = player_stats.get_player_stats(first_name, last_name)
        player_progress = player_stats.get_progress_from_player_stats(player_stats_response)
    except PlayerNotFoundException:
        error_message = 'No player found for the given name, {first_name} {last_name}'\
                        .format(first_name=first_name,
                                last_name=last_name)
        logger.error(error_message)
        return error_message

    return player_progress


if __name__ == "__main__":
    _configure_logger()

    parser = argparse.ArgumentParser()
    _configure_arg_parser()
    args = parser.parse_args()

    # Do action as per the argument
    if args.action == actions.TEAM_ROSTER_ACTION:
        name = args.name
        response = _get_team_roster(name)
        if response:
            formatted_response = tables.build_tables_from_json(TEAM_HEADERS, list(response))
            _show_results(formatted_response)
    elif args.action == actions.PLAYER_SUMMARY_ACTION:
        first_name, last_name = args.name.split(sep=" ", maxsplit=1)
        response = _get_player_stats(first_name,last_name)
        for stat_name, stats in response.items():
            print(StackedGraph(list(stats.keys()), list(stats.values()), stat_name))
        #print(json.dumps(response, indent=2))
