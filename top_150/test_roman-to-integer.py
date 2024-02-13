# https://leetcode.com/problems/roman-to-integer/
import pytest


class Solution(object):
    def romanToInt(self, s):
        sm = 0
        while len(s) > 0:
            s, v = self.getValue(s)
            sm += v
        return sm

    def getValue(self, s):
        if s[:2] == "CM":
            return s[2:], 900
        elif s[:2] == "CD":
            return s[2:], 400
        elif s[:2] == "XC":
            return s[2:], 90
        elif s[:2] == "XL":
            return s[2:], 40
        elif s[:2] == "IX":
            return s[2:], 9
        elif s[:2] == "IV":
            return s[2:], 4
        elif s[:1] == "M":
            return s[1:], 1000
        elif s[:1] == "D":
            return s[1:], 500
        elif s[:1] == "C":
            return s[1:], 100
        elif s[:1] == "L":
            return s[1:], 50
        elif s[:1] == "X":
            return s[1:], 10
        elif s[:1] == "V":
            return s[1:], 5
        elif s[:1] == "I":
            return s[1:], 1


@pytest.mark.parametrize("s, expected", [
    ("III", 3)])
def test_answer(s, expected):
    assert Solution().romanToInt(s) == expected
