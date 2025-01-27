
import re
import pandas as pd
import numpy as np
from collections import Counter
from aocd import get_data, submit


dat = get_data(day=5, year=2024).split('\n')

dat = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
""".split('\n')

rules = [r for r in dat if '|' in r]
pages = [p for p in dat if ',' in p]

