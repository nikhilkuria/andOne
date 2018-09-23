import logging

from nubia import command, argument

from teams import team_stats, TeamNotFoundException
from visual import tables
from constants import TEAM_HEADERS

logger = logging.getLogger('pynba.command.team')


@command
class Team:
    """Use this to see the team roster and other useful things about your favourite team"""

    @command
    @argument("team_name", positional=True)
    def roster(self, team_name: str):
        """
        print the players in the team roster
        """
        try:
            logger.info('Team roster action called on {name}'
                        .format(name=team_name))
            response = team_stats.get_team_roster(team_name)
            formatted_response = tables.build_tables_from_json(TEAM_HEADERS, list(response))
            print(formatted_response)
        except TeamNotFoundException:
            error_message = 'No team found for the given name {name}. ' \
                            'Use either the city name, franchise name or the 3 digit code'\
                            .format(name=team_name)
            logger.error(error_message)
            print(error_message)

