"""Module for logging functionality."""

import logging


def setup_logging(log_level: int = logging.INFO):
    """Set up logging format, suppressing specific packages."""
    to_suppress_packages = [""]
    for package in to_suppress_packages:
        logging.getLogger(package).setLevel(logging.WARNING)

    logging.basicConfig(
        level=log_level,
        format="%(asctime)s|%(levelname)s|%(name)s|%(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
