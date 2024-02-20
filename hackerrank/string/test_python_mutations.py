# https://www.hackerrank.com/challenges/python-mutations/problem
import pytest


def split_and_join(line):
    # write your code here
    return "-".join([a for a in line.split()])


@pytest.mark.parametrize("s, expected", [
    ('this is a string', 'this-is-a-string')])
def test_split_and_join(s, expected):
    assert split_and_join(s) == expected
