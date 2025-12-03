"""Module for Advent of Code 2025: Day 3."""

import logging
import os

from log import setup_logging


def read_puzzle_input() -> list:
    """Read puzzle input."""
    file_path = "../inputs"
    file_name = "day3.txt"

    file = open(os.path.join(file_path, file_name), "r")
    input_raw = file.read()
    file.close()
    return [x for x in input_raw.split("\n")]


def find_maximum_joltage_full_search(battery_bank: str) -> int:
    """Find maximum joltage of battery bank using full search."""
    max_joltage = 0
    # Loop over all battery combinations while keeping track of maximum joltage
    for i in range(0, len(battery_bank)):
        for j in range(i+1, len(battery_bank)):
            joltage = int(battery_bank[i] + battery_bank[j])
            if joltage > max_joltage:
                max_joltage = joltage
    return max_joltage


def find_maximum_joltage_skip_search(battery_bank: str) -> int:
    """Find maximum joltage of battery bank using skip search."""
    # Due to concatenation of digits, it is more beneficial to skip small/smaller digits
    # at the beginning of the battery bank. Therefore, select each time the largest digit
    # while keeping in mind the number of batteries we have to select. 
    n_choose = 12
    joltage = ""
    n = len(battery_bank)

    # Define a (dynamic) interval for the battery selection process. Keep track of the 
    # starting and ending index and maximum battery value we are looking for
    start = 0
    end = n - n_choose + 1
    maximum = max(battery_bank[start:end])
    
    i = 0
    while n_choose > 0:
        # If battery value matches the maximum within the interval, add this battery
        if battery_bank[i] == maximum:       
            joltage += str(battery_bank[i])
            n_choose -= 1
            
            # Stop searching if this was the last battery we had to pick
            if n_choose == 0:
                break
            
            # Update the dynamic interval by resetting the start, end and maximum of the interval
            start = i + 1
            end = n - n_choose + 1
            maximum = max(battery_bank[start:end])
            i = start
        else:
            i += 1

    return int(joltage)


def solve_day_three_part_one(input: list) -> int:
    """Solve day 3 part 1."""
    # Loop over all battery banks and keep track of the joltage
    joltages = []
    for battery_bank in input:
        joltages += [find_maximum_joltage_full_search(battery_bank)]
    return sum(joltages)


def solve_day_three_part_two(input: list) -> int:
    """Solve day 3 part 2."""
    # Loop over all battery banks and keep track of the joltage
    joltages = []
    for battery_bank in input:
        joltages += [find_maximum_joltage_skip_search(battery_bank)]
    return sum(joltages)


def main():
    """Entry point of code."""
    setup_logging()
    logging.info("Start of script.")

    input = read_puzzle_input()
    logging.info("Read puzzle input.")

    solution_part_one = solve_day_three_part_one(input)
    logging.info(f"Solved part 1! The total joltage output is: {solution_part_one}.")

    solution_part_two = solve_day_three_part_two(input)
    logging.info(f"Solved part 2! The total joltage output is: {solution_part_two}.")

    logging.info("End of script.")


if __name__ == "__main__":
    main()
