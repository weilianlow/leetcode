# https://leetcode.com/problems/reverse-words-in-a-string/submissions/
import pytest


class Solution(object):
    def reverseWords(self, s):
        return ' '.join(s.strip().split()[::-1])


@pytest.mark.parametrize("s, expected", [
    ("the sky is blue", "blue is sky the")])
def test_answer(s, expected):
    assert Solution().reverseWords(s) == expected
