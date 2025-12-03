"""Module for Advent of Code 2025: Day 2."""

import logging
import os

from math import floor

from log import setup_logging


def read_puzzle_input() -> list:
    """Read puzzle input."""
    file_path = "../inputs"
    file_name = "day2.txt"

    file = open(os.path.join(file_path, file_name), "r")
    input_raw = file.read()
    file.close()
    return [x for x in input_raw.replace("\n","").split(",")]


def is_strictly_repetitive(n: int) -> bool:
    """Check whether number if of the form <ab>-<ab>"""
    n = str(n)

    # If length of number is not a multiple of two, it cannot be strictly repetitive
    if len(n) % 2 != 0:
        return False
    
    # Split number into two equal parts and validate whether they are identical
    n_1, n_2 = n[:int(len(n)/2)], n[int(len(n)/2):]
    return n_1 == n_2


def solve_day_two_part_one(input: list) -> int:
    """Solve day 2 part 1."""
    # Loop over all product ranges and identify the allowed range of product IDs
    repetitive_numbers = []
    for product_range in input:
        # Split the product range into lower and upper bound for product ID
        product_ids = product_range.split("-")
        lower, upper = int(product_ids[0]), int(product_ids[1])
        allowed_range = range(lower, upper + 1)

        # Check for each number in this range whether it is strictly repetitive
        for n in allowed_range:
            if is_strictly_repetitive(n):
                repetitive_numbers += [int(n)]

    return sum(repetitive_numbers)


def is_approximately_repetitive(n: int) -> bool:
    """Check whether number is of the form <ab>-<ab><ab>."""
    # If number is strictly repetitive, return True
    if is_strictly_repetitive(n):
        return True
    
    n = str(n)
    # If not, split the number into smaller parts, start with the first digit only and check for repetitiveness
    # Continue this process until half the length of the number is reached.
    # There is no point in continuing afterwards, it won't be repetitive in that case.
    for i in range(0, floor(len(n) / 2)): 
        # Split number into 'first' and 'second' part. Duplicate the first part and validate whether it matches the second part.
        to_duplicate = n[:i+1]
        to_match = n[i+1:]

        if len(n) % len(to_duplicate) == 0:
            # Create duplicate of the first part of the correct length to match the second part
            duplicated = to_duplicate * int((len(n) - len(to_duplicate)) / len(to_duplicate))
            # If a repetitive pattern is found, stop immediately
            if duplicated == to_match:
                return True    
    return False


def solve_day_two_part_two(input: list) -> int:
    """Solve day 2 part 2."""
    # Loop over all product ranges and identify the allowed range of product IDs
    repetitive_numbers = []
    for product_range in input:
        # Split the product range into lower and upper bound for product ID
        product_ids = product_range.split("-")
        lower, upper = int(product_ids[0]), int(product_ids[1])
        allowed_range = range(lower, upper+1)

        # Check for each number in this range whether it is strictly repetitive
        for n in allowed_range:
            if is_approximately_repetitive(n):
                repetitive_numbers += [int(n)]

    return sum(repetitive_numbers)


def main():
    """Entry point of code."""
    setup_logging()
    logging.info("Start of script.")

    input = read_puzzle_input()
    logging.info("Read puzzle input.")

    solution_part_one = solve_day_two_part_one(input)
    logging.info(f"Solved part 1! The total sum of all valid IDs is: {solution_part_one}.")

    solution_part_two = solve_day_two_part_two(input)
    logging.info(f"Solved part 2! The total sum of all valid IDs is: {solution_part_two}.")

    logging.info("End of script.")


if __name__ == "__main__":
    main()
