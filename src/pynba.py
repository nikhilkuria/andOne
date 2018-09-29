#!/usr/bin/env python3

import sys, logging
from nubia import Nubia
from nubia_plugin import PyNbaPlugin


def _configure_logger():
    """
    Define the logging parameters
    """
    # Configure logging
    logger = logging.getLogger('pynba')
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler('../pynba.log')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)


# This is the entry point of the application.
# Sets the nubia plugin and starts the shell
if __name__ == "__main__":
    _configure_logger()
    plugin = PyNbaPlugin()
    shell = Nubia(name="py_nba", plugin=plugin)
    sys.exit(shell.run())
