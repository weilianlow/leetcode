# https://www.hackerrank.com/challenges/text-wrap/problem
import pytest


def wrap(string, max_width):
    v = [string[i:i + max_width] for i in range(0, len(string), max_width)]
    return '\n'.join(v)


answer = """ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ"""


@pytest.mark.parametrize("string, max_width, expected", [
    ('ABCDEFGHIJKLIMNOQRSTUVWXYZ', 4, answer)])
def test_wrap(string, max_width, expected):
    assert wrap(string, max_width) == expected
