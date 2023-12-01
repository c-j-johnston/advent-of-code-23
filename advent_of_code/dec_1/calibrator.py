import regex as re
import sys
from typing import List
import numpy as np

SPELLED_NUMS = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]
STRING_DIGITS = [str(i) for i in range(10)]
STRINGS_AND_WORDS = STRING_DIGITS + SPELLED_NUMS
DIGITS_DICT = {word: num for word, num in zip(SPELLED_NUMS, STRING_DIGITS)}


def sum_list(nums_list: List[int]) -> int:
    """Sums a list of integers."""
    return np.sum(nums_list)


def get_first_or_last_digit(
    cal_string: str, first_or_last: str, include_words: bool
) -> str:
    list_to_use = STRINGS_AND_WORDS if include_words else STRING_DIGITS
    assert first_or_last in ["first", "last"], "Specify first or last digit."
    all_text_nums = re.findall("|".join(list_to_use), cal_string, overlapped=True)
    return all_text_nums[0] if first_or_last == "first" else all_text_nums[-1]


def convert_to_digit_string(digit: str) -> str:
    try:
        return DIGITS_DICT[digit]
    except KeyError:
        return digit


def process_calibration_string(cal_string: str, include_words: bool) -> int:
    first = get_first_or_last_digit(cal_string, "first", include_words)
    last = get_first_or_last_digit(cal_string, "last", include_words)
    calibration_value = int(
        convert_to_digit_string(first) + convert_to_digit_string(last)
    )
    return calibration_value


def process_whole_input(cal_lines: List[str], include_words: bool) -> int:
    cal_values_list = [
        process_calibration_string(cal, include_words) for cal in cal_lines
    ]

    answer = sum_list(cal_values_list)

    return answer


if __name__ == "__main__":
    cal_document = sys.argv[1]

    check_for_spelled_nums = sys.argv[2]
    assert check_for_spelled_nums in ["0", "1"]

    cal_lines = [line.strip() for line in open(cal_document, "r").readlines()]

    answer = process_whole_input(cal_lines, bool(int(check_for_spelled_nums)))

    print(f"The sum of all calibration values is {answer}.")
