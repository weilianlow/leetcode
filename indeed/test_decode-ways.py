import pytest


class Solution(object):
    def numDecodings(self, s):
        if not s or s.startswith('0'):
            return 0
        stack = [1, 1]
        for i in range(1, len(s)):
            if s[i] == '0':
                if s[i - 1] == '0' or s[i - 1] > '2':  # only '10', '20' is valid
                    return 0
                stack.append(stack[-2])
            elif 9 < int(s[i - 1:i + 1]) < 27:  # '01 - 09' is not allowed
                stack.append(stack[-2] + stack[-1])
            else:  # other case '01, 09, 27'
                stack.append(stack[-1])
        return stack[-1]


@pytest.mark.parametrize("s, expected", [
    ("12", 2), ("226", 3,), ("06", 0)])
def test_answer(s, expected):
    assert Solution().numDecodings(s) == expected
