import logging
from typing import List

from nubia import command, argument

from players import player_stats, PlayerNotFoundException
from visual import stacked_graph

logger = logging.getLogger('pynba.command.player')


@command
class Player:
    """Use this to see stats and performance of your favourite player"""

    @command
    @argument("player_name", description="name of the player ", positional=True)
    @argument("stat_names", description="stats", choices=[
        "GAMES PLAYED",
        "GAMES STARTED",
        "MINUTES",
        "AVG POINTS",
        "AVG ASSISTS",
        "AVG REBOUNDS",
        "AVG STEALS",
        "AVG BLOCKS",
        "AVG TURNOVERS",
        "AVG PERSONAL FOULS"
    ])
    def year_on_year(self, player_name: str, stat_names: List[str] = None):
        """
        print the player's year on year statistics
        """
        first_name, last_name = player_name.split(sep=" ", maxsplit=1)

        try:
            logger.info('year on year action called on first_name = {first_name} and last_name = {last_name}'
                        .format(first_name=first_name,
                                last_name=last_name))

            player_stats_response = player_stats.get_player_stats(first_name, last_name)
            player_yoy = player_stats.get_progress_from_player_stats(player_stats_response)
            if stat_names:
                for stat_name in stat_names:
                    stats = player_yoy[stat_name]
                    print(stacked_graph.build_stacked_graph(list(stats.keys()), list(stats.values()), stat_name))
            else:
                for stat_name, stats in player_yoy.items():
                    print(stacked_graph.build_stacked_graph(list(stats.keys()), list(stats.values()), stat_name))
        except PlayerNotFoundException:
            error_message = 'No player found for the given name, {first_name} {last_name}'\
                            .format(first_name=first_name,
                                    last_name=last_name)
            logger.error(error_message)
            print(error_message)


