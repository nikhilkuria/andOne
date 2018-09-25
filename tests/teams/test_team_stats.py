from teams.team_stats import _match_team_from_input as match_team_from_input
from teams.team_stats import _parse_team_name as parse_team_name
from nba_py.constants import TEAMS


def test_team_name_found_city_name():
    for team_code, team in TEAMS.items():
        city = team['city']
        if city == 'Los Angeles':
            continue
        found_team = match_team_from_input(city.upper())
        assert team == found_team


def test_team_name_found_franchise_name():
    for team_code, team in TEAMS.items():
        franchise_name = team['name']
        found_team = match_team_from_input(franchise_name.upper())
        assert team == found_team


def test_team_name_found_team_code():
    for team_code, team in TEAMS.items():
        found_team_name, found_team_id = parse_team_name(team_code)

        team_name = "{city} {franchise}".format(city=team['city'], franchise=team['name'])
        team_id = team['id']

        assert found_team_name == team_name
        assert found_team_id == team_id


def test_team_name_not_found_exception_thrown():
    pass
