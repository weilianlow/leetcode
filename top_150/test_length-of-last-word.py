# https://leetcode.com/problems/length-of-last-word/
import pytest


class Solution(object):
    def lengthOfLastWord(self, s):
        return len(s.strip().split()[-1])


@pytest.mark.parametrize("s, expected", [
    ("Hello World", 5)])
def test_answer(s, expected):
    assert Solution().lengthOfLastWord(s) == expected
