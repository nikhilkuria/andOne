import pytest

from teams.team_stats import _match_team_from_input as match_team_from_input
from teams.team_stats import _parse_team_name as parse_team_name
from teams import TeamNotFoundException
from nba_py.constants import TEAMS


def test_team_name_found_from_city_name():
    """
    Tests if the team can be found from the name of the city
    """
    for team_code, team in TEAMS.items():
        city = team['city']
        if city == 'Los Angeles':
            continue
        found_team = match_team_from_input(city.upper())
        assert team == found_team


def test_team_name_found_from_franchise_name():
    """
    Tests if the team can be found from the name of the franchise
    """
    for team_code, team in TEAMS.items():
        franchise_name = team['name']
        found_team = match_team_from_input(franchise_name.upper())
        assert team == found_team


def test_team_name_found_from_team_code():
    """
    Tests if the team can found from the team code
    """
    for team_code, team in TEAMS.items():
        found_team_name, found_team_id = parse_team_name(team_code)

        team_name = "{city} {franchise}".format(city=team['city'], franchise=team['name'])
        team_id = team['id']

        assert found_team_name == team_name
        assert found_team_id == team_id


def test_team_name_not_found_exception_thrown():
    """
    Tests if an exception is thrown when the team is not found
    """
    with pytest.raises(TeamNotFoundException):
        parse_team_name("INVALID")
