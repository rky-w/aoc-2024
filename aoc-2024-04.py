
import re
import pandas as pd
import numpy as np
from collections import Counter
from aocd import get_data, submit


dat = get_data(day=4, year=2024)

# dat = """\
# MMMSXXMASM
# MSAMXMSMSA
# AMXSXMAAMM
# MSAMASMSMX
# XMASAMXAMM
# XXAMMXXAMA
# SMSMSASXSS
# SAXAMASAAA
# MAMMMXMMMM
# MXMXAXMASX\
# """

lkp = {'X': 0, 'M': 1, 'A': 2, 'S': 3}

arr = np.array([[lkp[x] for x in list(line)] for line in dat.split('\n')], dtype=int)


def count_sequence(arr, seq=[0, 1, 2, 3]):
    seq_len = len(seq)
    reverse_seq = seq[::-1]  # Reverse sequence: [3, 2, 1, 0]
    count = 0

    # Function to check if subarray matches either sequence
    def matches_subarray(subarr):
        return np.array_equal(subarr, seq) or np.array_equal(subarr, reverse_seq)

    # Check horizontal
    for row in arr:
        for i in range(len(row) - seq_len + 1):
            if matches_subarray(row[i:i + seq_len]):
                count += 1

    # Check vertical
    for col in range(arr.shape[1]):
        for i in range(arr.shape[0] - seq_len + 1):
            if matches_subarray(arr[i:i + seq_len, col]):
                count += 1

    # Check diagonal (top-left to bottom-right)
    for i in range(arr.shape[0] - seq_len + 1):
        for j in range(arr.shape[1] - seq_len + 1):
            if matches_subarray([arr[i + k, j + k] for k in range(seq_len)]):
                count += 1

    # Check anti-diagonal (top-right to bottom-left)
    for i in range(arr.shape[0] - seq_len + 1):
        for j in range(seq_len - 1, arr.shape[1]):
            if matches_subarray([arr[i + k, j - k] for k in range(seq_len)]):
                count += 1

    return count

# Count occurrences of [0, 1, 2, 3] or [3, 2, 1, 0]
count_result = count_sequence(arr)
count_result

# submit(count_result, part='a', day=4, year=2024)




# Part B

def count_mas(arr, seq=[1, 2, 3]):
    seq_len = len(seq)
    reverse_seq = seq[::-1]  # Reverse sequence: [3, 2, 1, 0]
    count = 0

    # Function to check if subarray matches either sequence
    def matches_subarray(subarr):
        return np.array_equal(subarr, seq) or np.array_equal(subarr, reverse_seq)

    # Check diagonal (top-left to bottom-right)
    for i in range(arr.shape[0] - seq_len + 1):
        for j in range(arr.shape[1] - seq_len + 1):
            if matches_subarray([arr[i + k, j + k] for k in range(seq_len)]):
                # Check orthogonal subarray
                if matches_subarray([arr[i + k, j + seq_len - 1 - k] for k in range(seq_len)]):
                    count += 1

    return count

mas_result = count_mas(arr)

submit(mas_result, part='b', day=4, year=2024)