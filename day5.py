"""Module for Advent of Code 2025: Day 5."""

import logging
import os

import pandas as pd

from log import setup_logging


def read_puzzle_input() -> list:
    """Read puzzle input."""
    file_path = "../inputs"
    file_name = "day5.txt"

    file = open(os.path.join(file_path, file_name), "r")
    input_raw = file.read()
    file.close()
    return [x for x in input_raw.split("\n\n")]


def get_fresh_ingredients(input: list) -> pd.DataFrame:
    """Extract fresh ingredient ranges from puzzle input."""
    ingredient_ranges = input[0].split("\n")
    return pd.DataFrame([
        [int(x.split("-")[0]) for x in ingredient_ranges],
        [int(x.split("-")[1]) for x in ingredient_ranges],
    ]).T


def get_ingredient_list(input: list) -> list:
    """Extract ingredient list from puzzle input."""
    return [int(x) for x in input[1].split("\n")]


def solve_day_five_part_one(ingredients_list: list, fresh_ingredients: pd.DataFrame) -> int:
    """Solve day 5 part 1."""
    # An ingredient is fresh if it is within the fresh ingredients range
    # That is, it is larger than the minimum and smaller than the maximum
    fresh = []
    for ingredient in ingredients_list:
        result = any((ingredient >= fresh_ingredients[0]) & (ingredient <= fresh_ingredients[1]))
        fresh += [result]
    return sum(fresh)


def solve_day_five_part_two(fresh_ingredients: pd.DataFrame) -> int:
    """Solve day 5 part 2."""
    # Loop through all fresh ingredients ranges and keep track of the ranges
    # Identify whether the ranges (partially) overlap and update the ranges accordingly
    product_ranges = pd.DataFrame(fresh_ingredients.iloc[0]).T

    for i in fresh_ingredients.index[1:]:
        lower, upper = fresh_ingredients.iloc[i,]
        
        # Check whether entire interval is already included in product_ranges
        if any((lower >= product_ranges[0]) & (upper <= product_ranges[1])) == True:
            continue

        # Identify whether this range partially or fully overlaps with another interval
        overlap_indices = (
            # Partial overlap on the left side
            product_ranges.index[(lower <= product_ranges[0]) & (upper >= product_ranges[0])].tolist()
            # Partial overlap on the right side
            + product_ranges.index[(lower <= product_ranges[1]) & (upper >= product_ranges[1])].tolist()
            # Complete overlap
            + product_ranges.index[(lower <= product_ranges[0]) & (upper >= product_ranges[1])].tolist()
        )

        # Deduplicate the indices
        overlap_indices = [i for i in set(overlap_indices)]

        if len(overlap_indices) == 0:
            # Add new interval to product ranges
            product_ranges = pd.concat([
                product_ranges,
                pd.Series([lower, upper]).to_frame().T
            ], ignore_index=True)
        else:
            # Fix overlapping product ranges by setting new lower and upper bound over entire interval
            overlapping_ranges = product_ranges.iloc[overlap_indices]
            overlapping_lower = min(overlapping_ranges[0].tolist() + [lower])
            overlapping_upper = max(overlapping_ranges[1].tolist() + [upper])

            # Remove overlapping indices from product_ranges and re-add new interval
            product_ranges = product_ranges.drop(overlap_indices)
            product_ranges = pd.concat([
                product_ranges,
                pd.Series([overlapping_lower, overlapping_upper]).to_frame().T
            ], ignore_index=True)

    return sum((product_ranges[1] - product_ranges[0]) + 1)


def main():
    """Entry point of code."""
    setup_logging()
    logging.info("Start of script.")

    input = read_puzzle_input()
    logging.info("Read puzzle input.")

    ingredients_list = get_ingredient_list(input)
    fresh_ingredients = get_fresh_ingredients(input)
    logging.info("Transformed puzzle input into ingredients list and fresh product ranges.")

    solution_part_one = solve_day_five_part_one(ingredients_list, fresh_ingredients)
    logging.info(f"Solved part 1! The: {solution_part_one}.")

    solution_part_two = solve_day_five_part_two(fresh_ingredients)
    logging.info(f"Solved part 2! The: {solution_part_two}.")

    logging.info("End of script.")


if __name__ == "__main__":
    main()
