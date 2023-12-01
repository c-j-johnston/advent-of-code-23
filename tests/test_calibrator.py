import pytest
from advent_of_code.dec_1.calibrator import (
    get_first_or_last_digit,
    convert_to_digit_string,
    process_whole_input,
)


@pytest.mark.parametrize(
    "input_string, first, last",
    [
        ("1abc2", "1", "2"),
        ("pqr3stu8vwx", "3", "8"),
        ("a1b2c3d4e5f", "1", "5"),
        ("treb7uchet", "7", "7"),
    ],
)
def test_get_first_and_last_part_one(input_string, first, last):
    assert get_first_or_last_digit(input_string, "first", False) == first
    assert get_first_or_last_digit(input_string, "last", False) == last


@pytest.mark.parametrize(
    "input_string, first, last",
    [
        ("two1nine", "two", "nine"),
        ("eightwothree", "eight", "three"),
        ("abcone2threexyz", "one", "three"),
        ("xtwone3four", "two", "four"),
        ("4nineeightseven2", "4", "2"),
        ("zoneight234", "one", "4"),
        ("7pqrstsixteen", "7", "six"),
    ],
)
def test_get_first_and_last_part_two(input_string, first, last):
    assert get_first_or_last_digit(input_string, "first", True) == first
    assert get_first_or_last_digit(input_string, "last", True) == last


@pytest.mark.parametrize("string, expected_output", [("one", "1"), ("3", "3")])
def test_convert_to_digit_string(string, expected_output):
    assert convert_to_digit_string(string) == expected_output


@pytest.mark.parametrize(
    "input_strings_list, expected_value, include_words",
    [
        (["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"], 142, False),  # Part 1
        (
            [
                "two1nine",
                "eightwothree",
                "abcone2threexyz",
                "xtwone3four",
                "4nineeightseven2",
                "zoneight234",
                "7pqrstsixteen",
            ],
            281,
            True,
        ),  # Part 2
    ],
)
def test_whole_process(input_strings_list, expected_value, include_words):
    assert process_whole_input(input_strings_list, include_words) == expected_value
