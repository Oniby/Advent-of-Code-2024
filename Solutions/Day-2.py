import re
from utils import *

def is_safe(report_str:str) -> bool:
    pattern = re.compile(r'\d+')
    m = re.findall(pattern, report_str)
    report = [int(l) for l in m]
    for i in range(1,len(report)):
        diff = report[i] - report[i-1]
        if diff*(report[1]-report[0])<0:
            return False
        elif abs(diff)<1 or abs(diff)>3:
            return False
    return True

puzzle_input = read_full_input(2, False)

n_safe = 0
for report in puzzle_input.split('\n'):
    if is_safe(report):
        n_safe += 1

print(f"There are {n_safe} safe reports.")
