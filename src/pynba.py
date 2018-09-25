#!/usr/bin/env python3

import sys
from nubia import Nubia
from nubia_plugin import PyNbaPlugin

# This is the entry point of the application.
# Sets the nubia plugin and starts the shell
if __name__ == "__main__":
    plugin = PyNbaPlugin()
    shell = Nubia(name="py_nba", plugin=plugin)
    sys.exit(shell.run())
