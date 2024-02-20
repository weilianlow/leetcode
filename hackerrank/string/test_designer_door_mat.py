# https://www.hackerrank.com/challenges/designer-door-mat/problem
import pytest


def designer_door_mat(row, width):
    pattern = list()
    for i in range(1, int(row / 2) + 1):
        trey = i * 2 - 1
        hypen = int((width - trey * 3) / 2)
        pattern.append('-' * hypen + '.|.' * trey + '-' * hypen)

    welcome = ['-' * int((width - 7) / 2) + 'WELCOME' + '-' * int((width - 7) / 2)]
    return '\n'.join(pattern + welcome + pattern[::-1])


answer = """------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------"""


@pytest.mark.parametrize("row, width, expected", [
    (9, 27, answer)])
def test_designer_door_mat(row, width, expected):
    assert designer_door_mat(row, width) == expected
