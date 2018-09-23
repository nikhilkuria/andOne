#!/usr/bin/env python3

import sys
from nubia import Nubia
from nubia_plugin import NubiaPlugin

if __name__ == "__main__":
    plugin = NubiaPlugin()
    shell = Nubia(name="py_nba", plugin=plugin)
    sys.exit(shell.run())
