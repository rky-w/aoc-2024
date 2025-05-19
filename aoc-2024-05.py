
import re
import pandas as pd
import numpy as np
from collections import Counter
from aocd import get_data, submit
import networkx as nx



dat = get_data(day=5, year=2024).split('\n')

# dat = """47|53
# 97|13
# 97|61
# 97|47
# 75|29
# 61|13
# 75|53
# 29|13
# 97|29
# 53|29
# 61|53
# 97|53
# 61|29
# 47|13
# 75|47
# 97|75
# 47|61
# 75|61
# 47|29
# 75|13
# 53|13

# 75,47,61,53,29
# 97,61,53,29,13
# 75,29,13
# 75,97,47,61,53
# 61,13,29
# 97,13,75,29,47
# """.split('\n')


## Get rules and updates

rules = [[int(x) for x in r.split('|')] for r in dat if '|' in r]
rev_rules = [r[::-1] for r in rules]

updates = [np.array(update.split(','), dtype=int) for update in dat if ',' in update]


# Function to check that subseq is present in seq, allowing for gaps
def is_ordered_subsequence(subseq, seq):
    it = iter(seq) # iter ensures that we only search forwards within seq each time 'x in it' is called
    return all(x in it for x in subseq)



midsum = 0
valid_pages = []
invalid_pages = []
for pages in updates:
    flag = 0
    for rr in rev_rules:
        if is_ordered_subsequence(rr, pages):
            flag = 1
            invalid_pages.append(pages)
            break
    if not flag:
        midsum += pages[len(pages) // 2]

print(f"Part 1 answer: {midsum}")
# submit(midsum, part='a', day=5, year=2024)


# Correct the invalid pages
invalid_pages
corrected_pages = []
for inv in invalid_pages:
    # Get all rules which are subsets of the pages in invalid pages
    vrules = []
    for rule in rules:
        if set(rule).issubset(set(inv)):
            vrules.append(rule)

    # Make use of topological sorting to find the order of pages
    # Create a directed graph where each rule is a path
    G = nx.DiGraph()
    for rule in vrules:
        nx.add_path(G, rule)
    ordered_pages = list(nx.topological_sort(G))
    corrected_pages.append(ordered_pages)


midsum2 = sum([x[len(x) // 2] for x in corrected_pages])


print(f"Part 2 answer: {midsum2}")
submit(midsum2, part='b', day=5, year=2024)

