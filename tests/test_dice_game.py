import pytest

from advent_of_code.dec_2.dice_game import (
    format_game_string,
    check_game_is_possible,
    get_game_id,
    create_game_dicts,
    sum_of_ids,
    get_minimum_dice,
    get_power,
    sum_of_game_powers,
)


@pytest.mark.parametrize(
    "game_string, game_id",
    [
        (
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
            1,
        ),
        ("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue", 2),
        (
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
            3,
        ),
        (
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
            4,
        ),
        ("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green", 5),
    ],
)
def test_get_game_id(game_string, game_id):
    assert get_game_id(game_string) == game_id


@pytest.mark.parametrize(
    "game_dict, is_possible",
    [
        (
            {"red": [4, 1, 0], "green": [0, 2, 2], "blue": [3, 6, 0]},
            True,
        ),
        ({"red": [0, 1, 0], "green": [2, 3, 1], "blue": [1, 4, 1]}, True),
        (
            {"red": [20, 4, 1], "green": [8, 13, 5], "blue": [6, 5, 0]},
            False,
        ),
        (
            {"red": [3, 6, 14], "green": [1, 3, 3], "blue": [6, 0, 15]},
            False,
        ),
        ({"red": [6, 1], "green": [3, 2], "blue": [1, 2]}, True),
    ],
)
def test_dice_game_possible(game_dict, is_possible):
    assert check_game_is_possible(game_dict) == is_possible


@pytest.mark.parametrize(
    "game_string, game_dict",
    [
        (
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
            {"red": [4, 1, 0], "green": [0, 2, 2], "blue": [3, 6, 0]},
        ),
        (
            "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
            {"red": [0, 1, 0], "green": [2, 3, 1], "blue": [1, 4, 1]},
        ),
        (
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
            {"red": [20, 4, 1], "green": [8, 13, 5], "blue": [6, 5, 0]},
        ),
        (
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
            {"red": [3, 6, 14], "green": [1, 3, 3], "blue": [6, 0, 15]},
        ),
        (
            "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
            {"red": [6, 1], "green": [3, 2], "blue": [1, 2]},
        ),
    ],
)
def test_format_game_string(game_string, game_dict):
    assert format_game_string(game_string) == game_dict


@pytest.mark.parametrize(
    "game_dict, minimum_dice, power",
    [
        (
            {"red": [4, 1, 0], "green": [0, 2, 2], "blue": [3, 6, 0]},
            {"red": 4, "green": 2, "blue": 6},
            48,
        ),
        (
            {"red": [0, 1, 0], "green": [2, 3, 1], "blue": [1, 4, 1]},
            {"red": 1, "green": 3, "blue": 4},
            12,
        ),
        (
            {"red": [20, 4, 1], "green": [8, 13, 5], "blue": [6, 5, 0]},
            {"red": 20, "green": 13, "blue": 6},
            1560,
        ),
        (
            {"red": [3, 6, 14], "green": [1, 3, 3], "blue": [6, 0, 15]},
            {"red": 14, "green": 3, "blue": 15},
            630,
        ),
        (
            {"red": [6, 1], "green": [3, 2], "blue": [1, 2]},
            {"red": 6, "green": 3, "blue": 2},
            36,
        ),
    ],
)
def test_minimum_and_power(game_dict, minimum_dice, power):
    assert get_minimum_dice(game_dict) == minimum_dice
    assert get_power(minimum_dice) == power


@pytest.mark.parametrize(
    "games_list, ids_total",
    [
        (
            [
                "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
                "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
                "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
                "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
                "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
            ],
            8,
        )
    ],
)
def test_whole_thing_part_one(games_list, ids_total):
    assert sum_of_ids(create_game_dicts(games_list)) == ids_total


@pytest.mark.parametrize(
    "games_list, total_power",
    [
        (
            [
                "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
                "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
                "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
                "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
                "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
            ],
            2286,
        )
    ],
)
def test_whole_thing_part_2(games_list, total_power):
    assert sum_of_game_powers(create_game_dicts(games_list)) == total_power
