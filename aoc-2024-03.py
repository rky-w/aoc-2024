
import re
import pandas as pd
import numpy as np
from collections import Counter
from aocd import get_data, submit


dat = get_data(day=3, year=2024)

p = re.compile(r'mul\(\d{1,3},\d{1,3}\)')
p2 = re.compile(r'\d+')

def multiplier(dat):
    ms = p.findall(dat)
    ans = 0
    for m in ms:
        r = p2.findall(m)
        ans += int(r[0]) * int(r[1])
    return ans

ans_a = multiplier(dat)

submit(ans_a, part='a', day=3, year=2024)


# pt b
p_do = re.compile(r"do\(\)")
p_dont = re.compile(r"don't\(\)")

datc = dat
tot = 0
while True:
    dont = p_dont.search(datc)
    if dont:
        tot += multiplier(datc[:dont.start()])
        datc = datc[dont.end():]
    else:
        tot += multiplier(datc)
        print('end tot', tot)
        break
    do = p_do.search(datc)
    if do:
        datc = datc[do.end():]
    else: 
        break

submit(tot, part='b', day=3, year=2024)