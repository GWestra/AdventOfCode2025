"""Module for Advent of Code 2025: Day 7."""

import logging
import os

from log import setup_logging


def read_puzzle_input() -> list:
    """Read puzzle input."""
    file_path = "../inputs"
    file_name = "day7.txt"

    file = open(os.path.join(file_path, file_name), "r")
    input_raw = file.read()
    file.close()
    return [x for x in input_raw.split("\n")]


def solve_day_seven_part_one(input: list) -> int:
    """Solve day 7 part 1."""
    # Identify the starting location(s) of the light particles
    start = [i for (i,x) in enumerate(input[0]) if x == "S"]

    # Keep track of the columns with downward beams and the number of splits
    beams = set(start)
    n_splits = 0

    # Simulate the light particle going through the puzzle. For each iteration,
    # check whether a splitter is hit and update downward beams and n_splits accordingly
    for i in range(1, len(input)):
        beams_to_add = set()
        beams_to_remove = set()

        for b in beams:
            if input[i][b] == "^":
                n_splits += 1
                beams_to_remove.add(b)
                beams_to_add.update([b-1, b+1])

        # Update the columns with light beams by removals and additions
        beams = (beams - beams_to_remove).union(beams_to_add)

    return n_splits


def solve_day_seven_part_two(input: list) -> int:
    """Solve day 7 part 2."""
    # Identify the starting location(s) of the light particles
    start = [i for (i,x) in enumerate(input[0]) if x == "S"]

    # Keep track of the columns with downward beams and the number of splits
    beams = set(start)
    n_splits = 0

    # Keep track of the number of paths that lead to each column
    paths = [0] * len(input[0])
    for s in start:
        paths[s] = 1

    # Simulate the light particle going through the puzzle and check whether a splitter is hit
    # in each iteration. If so, update columns with downward beams and n_splits accordingly
    for i in range(1, len(input)):
        beams_to_add = set()
        beams_to_remove = set()

        for b in beams:
            if input[i][b] == "^":
                n_splits += 1
                beams_to_remove.add(b)
                beams_to_add.update([b-1, b+1])

                # After a split, add the number of paths to left and right columns
                # Reset the number of paths after the splitter to zero
                paths[b-1] += paths[b]
                paths[b+1] += paths[b]
                paths[b] = 0

        # Update the columns with light beams by removals and additions
        beams = (beams - beams_to_remove).union(beams_to_add)

    return sum(paths)


def main():
    """Entry point of code."""
    setup_logging()
    logging.info("Start of script.")

    input = read_puzzle_input()
    logging.info("Read puzzle input.")

    solution_part_one = solve_day_seven_part_one(input)
    logging.info(f"Solved part 1! The: {solution_part_one}.")

    solution_part_two = solve_day_seven_part_two(input)
    logging.info(f"Solved part 2! The: {solution_part_two}.")

    logging.info("End of script.")


if __name__ == "__main__":
    main()
