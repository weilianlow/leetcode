# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
import pytest
from collections import defaultdict


def solve(arr):
    dct = defaultdict(set)
    for v in arr:
        name, score = v[0], v[1]
        dct[score].add(name)
    k = sorted(dct.keys())
    return '\n'.join(sorted(list(dct[k[1]])))


@pytest.mark.parametrize("arr, expected", [
    ([("Harry", 37.21), ("Berry", 37.21), ("Tina", 37.2), ("Akriti", 41), ("Harsh", 39)], "Berry\nHarry")])
def test_solve(arr, expected):
    assert solve(arr) == expected
