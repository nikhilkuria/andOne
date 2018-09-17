import logging

from nba_py import player

from .player_not_found_exception import PlayerNotFoundException

logger = logging.getLogger('pynba.player')


def get_player_stats(first_name, last_name):
    try:
        player_id = player.get_player(first_name, last_name)
        response = player.PlayerCareer(player_id).regular_season_totals()
    except StopIteration as error:
        logger.error("Could not find a player with the name - {first_name} {last_name}"
                     .format(first_name=first_name,
                             last_name=last_name))
        raise PlayerNotFoundException
    return response

