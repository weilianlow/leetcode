# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
import pytest


def solve(arr):
    result = set()
    for v in arr:
        result.add(v)
    return sorted(result)[-2]


@pytest.mark.parametrize("arr, expected", [
    ([2, 3, 6, 6, 5], 5)])
def test_solve(arr, expected):
    assert solve(arr) == expected
