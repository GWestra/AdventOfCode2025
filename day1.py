"""Module for Advent of Code 2025: Day 1."""

import logging
import os

from log import setup_logging


def read_puzzle_input() -> list:
    """Read puzzle input."""
    file_path = "../inputs"
    file_name = "day1.txt"

    file = open(os.path.join(file_path, file_name), "r")
    input_raw = file.read()
    file.close()
    return [x for x in input_raw.split("\n")]


def convert_input_to_rotations(input: list) -> list:
    """Convert list input to list of rotations to perform."""
    # Rotation to the left implies subtraction and to the right an addition
    result = [int(x.replace("L","-").replace("R","+")) for x in input] 
    return result


def solve_day_one_part_one(starting_value: int, rotations: list):
    """Solve day 1 part 1."""
    # Add starting value as the initial rotation
    rotations = [starting_value] + rotations

    # Calculate the positions of the dial after each rotation
    positions = [sum(rotations[0:i]) for i in range(1,len(rotations)+1)]

    # Check whether each position is an exact multiple of 100
    multiple_of_hundred = [p % 100 == 0 for p in positions]
    return sum(multiple_of_hundred)
    

def count_hundreds_in_between(a: int, b: int) -> int:
    """Count the number of multiples of hundred strictly between A and B."""
    # Return zero if A and B are identical
    if a == b:
        return 0
    
    # Make sure A is smaller than B
    if a > b:
        a, b = b, a
    
    # Find first multiple of 100 strictly greater than A
    start = ((a // 100) + 1) * 100

    # Find first multiple of 100 strictly smaller than B
    end = ((b - 1) // 100) * 100

    # Find number of hundreds between A and B, if any
    if start > end:
        return 0
    return (end - start) // 100 + 1


def solve_day_one_part_two(starting_value: int, rotations: list):
    """Solve day 1 part 2."""
    # Iterate over all rotations and check after each iteration
    # 1) Whether position after the rotation is a multiple of 100
    # 2) Number of hundreds that have been passed in between
    i = 0
    result = 0
    value = starting_value

    while i <= len(rotations)-1:
        previous_value = value
        value += rotations[i]

        if value % 100 == 0:
            result += 1

        hundred_count = count_hundreds_in_between(previous_value, value)
        result += hundred_count
        
        i += 1

    return result


def main():
    """Entry point of code."""
    setup_logging()
    logging.info("Start of script.")

    input = read_puzzle_input()
    logging.info("Read puzzle input.")

    rotations = convert_input_to_rotations(input)
    logging.info("Converted puzzle input to list of rotations.")

    starting_value = 50
    logging.info("Initialised the dial to starting position.")

    solution_part_one = solve_day_one_part_one(starting_value, rotations)
    logging.info(f"Solved part 1! The password to open the door is: {solution_part_one}.")
    
    solution_part_two = solve_day_one_part_two(starting_value, rotations)
    logging.info(f"Solved part 2! The password to open the door is: {solution_part_two}.")

    logging.info("End of script.")


if __name__ == "__main__":
    main()
