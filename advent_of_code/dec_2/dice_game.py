from typing import Dict, List
from dataclasses import dataclass

ACTUAL_DICE_COUNTS = {"red": 12, "green": 13, "blue": 14}

example_string = (
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
)


def get_game_id(game_string: str) -> int:
    return int(game_string.split(":")[0].split(" ")[-1])


def add_missing_blanks(
    games_dict: Dict[str, List[int]], intended_length: int
) -> Dict[str, List[int]]:
    for colour, counts in games_dict.items():
        if len(counts) < intended_length:
            games_dict[colour].append(0)
    return games_dict


def format_game_string(
    game_string: str,
    actual_dice_counts: Dict[str, int] = ACTUAL_DICE_COUNTS,
) -> Dict[str, List[int]]:
    games_dict = {colour: [] for colour in actual_dice_counts.keys()}
    reveals_list = game_string.split(":")[-1].split(";")
    for i, reveal in enumerate(reveals_list):
        colour_split = [split.strip() for split in reveal.split(",")]
        for num_and_colour in colour_split:
            num, colour = num_and_colour.split(" ")[:]
            games_dict[colour].append(int(num))
        games_dict = add_missing_blanks(games_dict, i + 1)
    return games_dict


def check_game_is_possible(
    game_dict: Dict[str, List[int]],
    actual_dice_counts: Dict[str, int] = ACTUAL_DICE_COUNTS,
) -> bool:
    for colour, maximum in actual_dice_counts.items():
        if colour in game_dict.keys():
            if max(game_dict[colour]) > maximum:
                return False
    return True


def get_minimum_dice(game_dict: Dict[str, List[int]]) -> Dict[str, int]:
    minimum_dice = {colour: max(dice) for colour, dice in game_dict.items()}
    return minimum_dice


def get_power(minimum_dice: Dict[str, int]) -> int:
    power = 1
    for minimum in minimum_dice.values():
        power *= minimum
    return power


@dataclass
class DiceGame:
    game_id: int
    game_string: str
    game_dict: Dict[str, List[int]]
    is_possible: bool
    actual_dice: Dict[str, int]
    game_power: int
    minimum_dice_needed: Dict[str, int]

    def __init__(self, game_string) -> None:
        self.game_string = game_string
        self.game_id = get_game_id(self.game_string)
        self.actual_dice = ACTUAL_DICE_COUNTS

    def process_string(self) -> None:
        self.game_dict = format_game_string(self.game_string)
        self.is_possible = check_game_is_possible(self.game_dict, self.actual_dice)
        self.minimum_dice_needed = get_minimum_dice(self.game_dict)
        self.power = get_power(self.minimum_dice_needed)


def sum_of_ids(all_games: Dict[int, Dict[str, bool | int]]) -> int:
    total = 0
    for id, results in all_games.items():
        if results["is_possible"]:
            total += id
    return total


def get_results_dict(games_list: List[str]) -> Dict[int, Dict[str, bool | int]]:
    all_games = {}
    for game in games_list:
        dice_game = DiceGame(game)
        dice_game.process_string()
        all_games[dice_game.game_id] = {
            "is_possible": dice_game.is_possible,
            "power": dice_game.power,
        }
    return all_games


def sum_of_game_powers(all_games: Dict[int, Dict[str, bool | int]]) -> int:
    power_sum = 0
    for results in all_games.values():
        power_sum += results["power"]
    return power_sum


if __name__ == "__main__":
    games_list = [
        line.strip()
        for line in open("advent_of_code/dec_2/dice_game_input.txt").readlines()
    ]

    all_games_results = get_results_dict(games_list)

    answer_one = sum_of_ids(all_games_results)

    print(f"The sum of IDs of posible games is {answer_one}.")

    answer_two = sum_of_game_powers(all_games_results)

    print(f"The sum of IDs of posible games is {answer_two}.")
