import re
import sys

if __name__ == "__main__":
    cal_document = sys.argv[1]

    cal_lines = open(cal_document, "r").readlines()

    nums = []
