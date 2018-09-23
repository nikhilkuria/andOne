from nubia import PluginInterface
from nubia.internal.cmdbase import AutoCommand

from commands import Team, Player


class NubiaPlugin(PluginInterface):

    def get_commands(self):
        return [
            AutoCommand(Team),
            AutoCommand(Player)
        ]
