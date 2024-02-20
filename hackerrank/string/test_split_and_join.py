# https://www.hackerrank.com/challenges/python-string-split-and-join/problem
import pytest


def mutate_string(string, position, character):
    return string[:position] + character + string[position + 1:]


@pytest.mark.parametrize("string, position, character, expected", [
    ('abracadabra', 5, 'k', 'abrackdabra')])
def test_mutate_string(string, position, character, expected):
    assert mutate_string(string, position, character) == expected
