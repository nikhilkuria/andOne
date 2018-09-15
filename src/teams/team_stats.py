import logging

from nba_py import team
from nba_py.constants import TEAMS

from constants import common
from teams import TeamNotFoundException

logger = logging.getLogger('pynba.teams')


def _match_team_from_input(team_name_input):
    """
    iterate through the list of teams to find a match
    from the team_name_input
    :param team_name_input:
    """
    for team_code in TEAMS:
        team_details = TEAMS[team_code]

        city = team_details['city'].upper()
        franchise = team_details['name'].upper()

        if team_name_input == city or team_name_input == franchise:
            return team_details

    return None


def _parse_team_name(team_name_input):
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

    if team_name_input in TEAMS:
        team_record = TEAMS[team_name_input]
    else:
        team_record = _match_team_from_input(team_name_input)

    if team_record is None:
        logger.error("Could not map the input {input} to a known team".format(input=team_name_input))
        raise TeamNotFoundException

    team_name = "{city} {franchise}".format(city=team_record['city'], franchise=team_record['name'])
    team_id = team_record['id']

    return team_name, team_id


def get_team_roster(team_name_input):
    team_name, team_id = _parse_team_name(team_name_input)
    logger.info('Fetching roster for team {team_name}'.format(team_name=team_name))

    team_details = team.TeamCommonRoster(team_id, common.SEASON)

    return team_details.roster()

