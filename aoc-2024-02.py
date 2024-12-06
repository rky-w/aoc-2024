
import pandas as pd
import numpy as np
from collections import Counter
from aocd import get_data, submit


dat = get_data(day=2, year=2024)

reps = [[int(it) for it in el.split(' ')] for el in dat.split('\n')]


# reps = [
#     [7, 6, 4, 2, 1],
#     [1, 2, 7, 8, 9],
#     [9, 7, 6, 2, 1],
#     [1, 3, 2, 4, 5],
#     [8, 6, 4, 4, 1],
#     [1, 3, 6, 7, 9],
# ]



# Part a

def check_safe(lst):
    arr = np.array([j-i for i, j in zip(lst[:-1], lst[1:])])
    return all((arr >= 1) & (arr <= 3)) | all((arr >= -3) & (arr <= -1))

safe_a = 0
for lst in reps:
    safe_a += check_safe(lst)

safe_a

submit(safe_a, part="a", day=2, year=2024)

# Part b

safe_b = 0
for lst in reps:
    if not check_safe(lst):
        for i in range(len(lst)):
            if check_safe(lst[:i] + lst[i+1:]):
                safe_b += 1
                break
    else:
        safe_b += 1

safe_b

submit(safe_b, part='b', day=2, year=2024)
