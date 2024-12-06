
import pandas as pd
import numpy as np
from collections import Counter
from aocd import get_data, submit


dat = get_data(day=1)

# Part a
arr = np.array([el.split('   ') for el in dat.split('\n')], dtype=int)

l1 = arr[:, 0]
l2 = arr[:, 1]

l1.sort()
l2.sort()

ans_a = sum(abs(l1 - l2))

submit(ans_a, part="a", day=1, year=2024)

# Part b

d = Counter(list(l2))
ans_b = sum([el * d[el] for el in set(l1).intersection(set(l2))])

submit(ans_b, part='b', day=1, year=2024)
