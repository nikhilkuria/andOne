import logging
from collections import defaultdict
from typing import Dict, List, DefaultDict

from nba_api.stats.endpoints.playercareerstats import PlayerCareerStats
from nba_api.stats.static import players as PlayerHelper
from nba_api.stats.library.parameters import PerModeSimple

from .player_not_found_exception import PlayerNotFoundException
from .multiple_players_found_exception import MultiplePlayersFoundException

logger = logging.getLogger('pynba.player')

def _format_results(raw_response: List[Dict]) -> Dict:
    response = dict()
    for entry in raw_response:
        season = entry['SEASON_ID']
        season_stats = dict()
        season_stats['GAMES PLAYED'] = entry['GP']
        season_stats['GAMES STARTED'] = entry['GS']
        season_stats['MINUTES'] = entry['MIN']
        season_stats['AVG POINTS'] = entry['PTS']
        season_stats['AVG ASSISTS'] = entry['AST']
        season_stats['AVG REBOUNDS'] = entry['REB']
        season_stats['AVG STEALS'] = entry['STL']
        season_stats['AVG BLOCKS'] = entry['BLK']
        season_stats['AVG TURNOVERS'] = entry['TOV']
        season_stats['AVG PERSONAL FOULS'] = entry['PF']
        response[season] = season_stats
    return response


def get_player_stats(first_name: str, last_name: str) -> Dict:
    """
    Returns the stats for a player in standard format
    :param first_name:
    :param last_name:
    :return:
    """
    players = PlayerHelper.find_players_by_full_name("{first_name} {last_name}".format(
        first_name=first_name,
        last_name=last_name
    ))

    if len(players) > 1 :
        logger.error("Multiple players found with the name - {first_name} {last_name}"
         .format(first_name=first_name,
                 last_name=last_name))
        raise MultiplePlayersFoundException
    if len(players) == 0:
        logger.error("Could not find a player with the name - {first_name} {last_name}"
         .format(first_name=first_name,
                 last_name=last_name))
        raise PlayerNotFoundException

    player_id = players[0]['id']

    logger.info("Fetching the player id for {first_name}, {last_name} - {player_id}"
                .format(first_name=first_name,
                        last_name=last_name,
                        player_id=player_id))

    all_player_stats = PlayerCareerStats(player_id, PerModeSimple.per_game).get_normalized_dict()
    yoy_stats = all_player_stats['SeasonTotalsRegularSeason']

    player_stats = _format_results(yoy_stats)

    return player_stats


def get_player_yoy_stats(first_name: str, last_name: str) -> DefaultDict:
    """
    Returns the Year on Year stats for a player
    :param first_name:
    :param last_name:
    :return:
    """
    yoy_stats = defaultdict(dict)
    player_stats = get_player_stats(first_name=first_name, last_name=last_name)

    for season, season_stats in player_stats.items():
        for stat_name, stats_value in season_stats.items():
            yoy_stats[stat_name][season] = stats_value

    return yoy_stats
