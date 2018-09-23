import logging
from collections import defaultdict
from typing import Dict, List, DefaultDict

from nba_py import player

from .player_not_found_exception import PlayerNotFoundException

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
    try:
        player_id = player.get_player(first_name, last_name)
        logger.info("Fetching the player id for {first_name}, {last_name} - {player_id}"
                    .format(first_name=first_name,
                            last_name=last_name,
                            player_id=player_id))

        raw_response = player.PlayerCareer(player_id).regular_season_totals()
    except StopIteration:
        logger.error("Could not find a player with the name - {first_name} {last_name}"
                     .format(first_name=first_name,
                             last_name=last_name))
        raise PlayerNotFoundException
    logger.info("Formatting the raw response for {first_name}, {last_name}"
                .format(first_name=first_name,
                        last_name=last_name))

    response = _format_results(raw_response)

    return response


def get_progress_from_player_stats(response: str) -> DefaultDict:
    progress_stats = defaultdict(dict)
    for season, season_stats in response.items():
        for stat_name, stats_value in season_stats.items():
            progress_stats[stat_name][season] = stats_value

    return progress_stats
