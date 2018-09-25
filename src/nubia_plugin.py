from nubia import PluginInterface
from nubia.internal.cmdbase import AutoCommand

from commands import Team, Player


class PyNbaPlugin(PluginInterface):

    def get_commands(self):
        """
        The following commands are supported at the moment
        - Team
        - Player
        :return: The list of commands
        """
        return [
            AutoCommand(Team),
            AutoCommand(Player)
        ]
