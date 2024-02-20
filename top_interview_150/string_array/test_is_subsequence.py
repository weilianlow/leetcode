# https://leetcode.com/problems/is-subsequence/
import pytest


class Solution(object):
    def isSubsequence(self, s, t):
        if len(s) == 0:
            return True
        lm, p = len(s), 0
        for v in t:
            if p == lm:
                return True
            if s[p] == v:
                p += 1
        if p == lm:
            return True
        return False


@pytest.mark.parametrize("s, t, expected", [
    ("abc", "ahbgdc", True)])
def test_answer(s, t, expected):
    assert Solution().isSubsequence(s, t) == expected
