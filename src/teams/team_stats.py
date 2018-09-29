import logging,json
from typing import Tuple

from nba_api.stats.endpoints.commonteamroster import CommonTeamRoster

from constants import TEAMS, SEASON
from teams import TeamNotFoundException

logger = logging.getLogger('pynba.teams')


def _match_team_from_input(team_name_input: str) -> str:
    """
    iterate through the list of teams to find a match
    from the team_name_input
    :param team_name_input: the team name as city name, franchise name, or team code in upper case
    """
    # Check if it's the team code, then read directly from the constants
    if team_name_input in TEAMS:
        team_details = TEAMS[team_name_input]
        return team_details

    # Else, see it it's a city name or a franchise name
    else:
        for team_code in TEAMS:
            team_details = TEAMS[team_code]

            city = team_details['city'].upper()
            franchise = team_details['name'].upper()
            if team_name_input == city or team_name_input == franchise:
                return team_details

    logger.error("Could not map the input {input} to a known team".format(input=team_name_input))
    raise TeamNotFoundException


def _parse_team_name(team_name_input: str) -> Tuple[str, int]:
    """
    Map the team_name input to a known team
    The input can be one of the following
    - The three digit code for the team ex: OKC, GSW
    - The city of the team ex: Chicago, Denver
    - The name of the franchise ex: Bulls, Bucks
    :param team_name_input:
    :return: team_name, team_id
    """
    team_name_input = team_name_input.upper()

    team_record = _match_team_from_input(team_name_input)

    team_name = "{city} {franchise}".format(city=team_record['city'], franchise=team_record['name'])
    team_id = team_record['id']

    return team_name, team_id


def get_team_roster(team_name_input: str) -> str:
    """
    from a given input of a team name, return the current roster as a json string
    can throw TeamNotFoundException
    :param team_name_input:
    :return: team name and team roster as string
    """
    team_name, team_id = _parse_team_name(team_name_input)
    logger.info('Fetching roster for team {team_name}'.format(team_name=team_name))

    team_details = CommonTeamRoster(team_id, SEASON).get_normalized_dict()
    return team_name, team_details["CommonTeamRoster"]

