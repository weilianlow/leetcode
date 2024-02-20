# https://www.hackerrank.com/challenges/swap-case/problem
import pytest


def swap_case(s):
    return ''.join([a.lower() if 65 <= ord(a) <= 90 else a.upper() for a in s])


@pytest.mark.parametrize("s, expected", [
    ('HackerRank.com presents "Pythonist 2".', 'hACKERrANK.COM PRESENTS "pYTHONIST 2".')])
def test_swap_case(s, expected):
    assert swap_case(s) == expected
