#!/usr/bin/python
import logging


def _configure_logger():
    # Configure logging
    logger = logging.getLogger('pynba')
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler('pynba.log')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)


if __name__ == "__main__":
    _configure_logger()

    cli_logger = logging.getLogger('pynba.cli')
    cli_logger.info("Welcome to pynba")
