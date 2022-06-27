import pytest


class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        lengths = [[x for x in range(len(text1) + 1)] for y in range(len(text2) + 1)]
        # set initial values
        for i in range(1, len(text1) + 1):
            lengths[0][i] = 0
        # what our table looks like
        """
        [     '' a  b  c  d  e
           ''[0, 0, 0, 0, 0, 0], 
           a [0, 1, 2, 3, 4, 5], 
           c [0, 1, 2, 3, 4, 5], 
           e [0, 1, 2, 3, 4, 5]
        ]
        """
        for i in range(1, len(text2) + 1):
            for j in range(1, len(text1) + 1):
                if text1[j - 1] == text2[i - 1]:
                    lengths[i][j] = 1 + lengths[i - 1][j - 1]
                else:
                    lengths[i][j] = max(lengths[i - 1][j], lengths[i][j - 1])
        return lengths[-1][-1]


@pytest.mark.parametrize("text1, test2, expected", [
    ("abcde", "ace", 3),
    ("abc", "abc", 3),
    ("abc", "def", 0)])
def test_answer(text1, test2, expected):
    assert Solution().longestCommonSubsequence(text1, test2) == expected
