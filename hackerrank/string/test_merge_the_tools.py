# https://www.hackerrank.com/challenges/merge-the-tools/problem
import pytest


def merge_the_tools(string, k):
    # your code goes here
    s = set()
    tmp = ''
    result = list()
    for i in range(len(string)):
        if i % k == 0 and i > 0:
            result.append(tmp)
            s = set()
            tmp = ''
        if string[i] not in s:
            tmp = tmp + string[i]
            s.add(string[i])
    result.append(tmp)
    return '\n'.join(result)


answer = """AB
CA
AD"""


@pytest.mark.parametrize("string, k, expected", [
    ('AABCAAADA', 3, answer)])
def test_merge_the_tools(string, k, expected):
    assert merge_the_tools(string, k) == expected
