# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
import pytest


class Solution(object):
    def strStr(self, haystack, needle):
        ln = len(needle)
        for i in range(len(haystack)):
            if haystack[i:i + ln] == needle:
                return i
        return -1


@pytest.mark.parametrize("haystack, needle, expected", [
    ("sadbutsad", "sad", 0)])
def test_answer(haystack, needle, expected):
    assert Solution().strStr(haystack, needle) == expected
