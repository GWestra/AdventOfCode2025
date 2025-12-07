"""Module for Advent of Code 2025: Day 6."""

import logging
import os

import numpy as np
import pandas as pd

from log import setup_logging


def read_puzzle_input() -> list:
    """Read puzzle input."""
    file_path = "../inputs"
    file_name = "day6.txt"

    file = open(os.path.join(file_path, file_name), "r")
    input_raw = file.read()
    file.close()
    return [x for x in input_raw.split("\n")]
    

def solve_day_six_part_one(input: list) -> int:
    """Solve day 6 part 1."""
    # Extract the operations and blocks of numbers from the puzzle input
    operations = [x for x in input[-1].split(" ") if x != ""]
    numbers = pd.DataFrame([list(map(int, line.split())) for line in input[:-1]])

    # Loop over all blocks of numbers and perform the corresponding operation
    # If operator is "+" or "*" take the sum or the product over entire column respectively
    result = []
    for i in range(0, len(operations)):
        if operations[i] == "+":
            result += [sum(numbers[i])]
        elif operations[i] == "*":
            result += [int(np.prod(numbers[i]))]

    return sum(result)


def solve_day_six_part_two(input: list) -> int:
    """Solve day 6 part 2."""
    # Split the puzzle input in operations and numbers. The numbers cannot be transformed
    # into a dataframe here, since we need the location of whitespaces within each block.
    operations = input[-1]
    numbers = input[:-1]

    # Loop over all columns right-to-left and keep track of the digits in each column
    # and the corresponding operator. If a operator is identified, execute the operation
    operator = operations[0]
    result = []
    values = []

    for i in range(len(operations)-1, -1, -1):
        # Extract all digits in the current column top-to-bottom
        digits = "".join([n[i] for n in numbers if n[i] != " "])
        if digits == "":
            continue

        # Update the digits and the operator found in this column
        values += [int(digits)]
        operator = operations[i]

        # Check whether we have to perform an operation
        if operator == " ":
            continue
        elif operator == "+":
            result += [sum(values)]
        elif operator == "*":
            result += [int(np.prod(values))]
        
        # Reset the identified values for next operation
        values = []
    
    return sum(result)


def main():
    """Entry point of code."""
    setup_logging()
    logging.info("Start of script.")

    input = read_puzzle_input()
    logging.info("Read puzzle input.")

    solution_part_one = solve_day_six_part_one(input)
    logging.info(f"Solved part 1! The grand total of all individual problems is: {solution_part_one}.")

    solution_part_two = solve_day_six_part_two(input)
    logging.info(f"Solved part 2! The grand total of all individual problems is: {solution_part_two}.")

    logging.info("End of script.")


if __name__ == "__main__":
    main()
