# https://www.hackerrank.com/challenges/capitalize/problem
import pytest


def solve(s):
    return ' '.join([''.join([v[i].upper() if i == 0 else v[i] for i in range(len(v))]) for v in s.split()])


@pytest.mark.parametrize("s, expected", [
    ('hello world', 'Hello World')])
def test_solve(s, expected):
    assert solve(s) == expected
