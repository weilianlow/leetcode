# https://leetcode.com/problems/insert-delete-getrandom-o1/
import pytest


class Solution(object):
    def isPalindrome(self, s):
        t = [v.lower() for v in s if v.isalnum()]

        i, j = 0, len(t) - 1

        while i < j:
            if t[i] != t[j]:
                return False
            i += 1
            j -= 1
        return True


@pytest.mark.parametrize("s, expected", [
    ("A man, a plan, a canal: Panama", True)])
def test_answer(s, expected):
    assert Solution().isPalindrome(s) == expected
