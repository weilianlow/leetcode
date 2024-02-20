# https://www.hackerrank.com/challenges/whats-your-name/problem
import pytest


def print_full_name(first, last):
    return f"Hello {first} {last}! You just delved into python."


@pytest.mark.parametrize("first, last, expected", [
    ('Ross', 'Taylor', 'Hello Ross Taylor! You just delved into python.')])
def test_print_full_name(first, last, expected):
    assert print_full_name(first, last) == expected
