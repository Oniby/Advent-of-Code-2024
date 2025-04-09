import re
from utils import *

def is_safe(report: list[int]):
    for i in range(1, len(report)):
        diff = report[i] - report[i - 1]
        if diff * (report[1] - report[0]) < 0:
            return False
        elif abs(diff) < 1 or abs(diff) > 3:
            return False
    return True

def report_from_string(report_string: str):
    pattern = re.compile(r'\d+')
    m = re.findall(pattern, report_string)
    report = [int(l) for l in m]
    return report

if __name__ == "__main__":

    part = 'B'

    if part == 'A':
        ### PART A
        puzzle_input = read_full_input(2, False)

        n_safe = 0
        for report_str in puzzle_input.split('\n'):
            report = report_from_string(report_str)
            if is_safe(report):
                n_safe += 1

        print(f"There are {n_safe} safe reports.")

    ### PART B
    if part == 'B':

        puzzle_input = read_full_input(2, False)

        n_safe = 0
        for report_str in puzzle_input.split('\n'):
            report = report_from_string(report_str)
            if is_safe(report):
                n_safe += 1
                continue
            for i in range(len(report)):
                cut_report = report[:i] + report[i + 1:]
                if is_safe(cut_report):
                    n_safe += 1
                    break

        print(f"There are {n_safe} safe reports.")
