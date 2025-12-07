"""Module for Advent of Code 2025: Day 4."""

import logging
import os

import pandas as pd
from warnings import simplefilter

from log import setup_logging


def read_puzzle_input() -> list:
    """Read puzzle input."""
    file_path = "../inputs"
    file_name = "day4.txt"

    file = open(os.path.join(file_path, file_name), "r")
    input_raw = file.read()
    file.close()
    return [x for x in input_raw.replace(".","0").replace("@","1").split("\n")]


def transform_input_into_grid(input: list) -> pd.DataFrame:
    """Transform list of input strings into grid."""
    result = []
    for i in range(0, len(input)):
        result.append([int(c) for c in input[i]])
    return pd.DataFrame(result)


def identify_number_of_neighbouring_rolls(df: pd.DataFrame) -> pd.DataFrame:
    """Identify the number of neighbouring rolls for each position."""
    # Shift the original dataframe both along the horizontal and vertical axis 
    # simultaneously and take the summation over all dataframes. Start with the
    # original dataframe multiplied by -1 to ignore the current position.
    result = -df
    for h in [-1,0,1]: # horizontal offset
        for v in [-1,0,1]: # vertical offset
            result += df.shift(periods=v, axis=0).shift(periods=h, axis=1).fillna(0)
    return result


def solve_day_four_part_one(grid: pd.DataFrame) -> int:
    """Solve day 4 part 1."""
    # Rolls of paper can be removed if number of neighbours is smaller than 4
    neighbours = identify_number_of_neighbouring_rolls(grid)
    return ((neighbours < 4) & (grid == 1)).sum(axis=1).sum(axis=0)


def solve_day_four_part_two(grid: list) -> int:
    """Solve day 4 part 2."""
    n_rolls = grid.sum(axis=1).sum(axis=0)

    # Iteratively remove paper rolls and update the grid afterwards
    while True:
        neighbours = identify_number_of_neighbouring_rolls(grid)
        rolls_to_remove = ((neighbours < 4) & grid == 1)

        # Stop once we can no longer remove any paper rolls
        if rolls_to_remove.sum(axis=1).sum(axis=0) == 0:
            break

        grid -= rolls_to_remove
    
    # Return total number of paper rolls that have been removed
    return n_rolls - grid.sum(axis=1).sum(axis=0)


def main():
    """Entry point of code."""
    setup_logging()
    simplefilter(action="ignore", category=pd.errors.PerformanceWarning)
    logging.info("Start of script.")

    input = read_puzzle_input()
    logging.info("Read puzzle input.")

    grid = transform_input_into_grid(input)
    logging.info("Transformed puzzle input into grid.")

    solution_part_one = solve_day_four_part_one(grid)
    logging.info(f"Solved part 1! The total number of rolls that can be removed is: {solution_part_one}.")

    solution_part_two = solve_day_four_part_two(grid)
    logging.info(f"Solved part 2! The total number of rolls that have been removed is: {solution_part_two}.")

    logging.info("End of script.")


if __name__ == "__main__":
    main()
