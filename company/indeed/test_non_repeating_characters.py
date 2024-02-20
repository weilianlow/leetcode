import pytest
from collections import OrderedDict

"""
https://algodaily.com/challenges/find-first-non-repeating-character
You're given a string of random alphanumerical characters with a length between 0 and 1000.
Write a method to return the first character in the string that does not repeat itself later on.
"""


class Solution(object):
    def firstNonRepeat(self, s):
        dct = OrderedDict()
        for char in s:
            if dct.get(char, None):
                dct[char] += 1
            else:
                dct[char] = 1

        for key in dct:
            if dct[key] == 1:
                return key
        return None


@pytest.mark.parametrize("s, expected", [
    ('asdfsdafdasfjdfsafnnunl', 'j')])
def test_answer(s, expected):
    assert Solution().firstNonRepeat(s) == expected
