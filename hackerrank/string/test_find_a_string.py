# https://www.hackerrank.com/challenges/find-a-string/problem
import pytest


def count_substring(string, sub_string):
    cnt = 0
    length = len(sub_string)
    for i in range(len(string)):
        if string[i:i + length] == sub_string:
            cnt += 1
    return cnt


@pytest.mark.parametrize("string, sub_string, expected", [
    ('ABCDCDC', 'CDC', 2)])
def test_count_substring(string, sub_string, expected):
    assert count_substring(string, sub_string) == expected
