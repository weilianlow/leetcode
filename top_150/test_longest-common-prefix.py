# https://leetcode.com/problems/longest-common-prefix/
import pytest


class Solution(object):
    def longestCommonPrefix(self, strs):
        mn = min([len(v) for v in strs])
        result = list()
        for i in range(mn):
            v = strs[0][i]
            for w in strs:
                if v != w[i]:
                    return ''.join(result)
            result.append(v)
        return ''.join(result)


@pytest.mark.parametrize("strs, expected", [
    (["flower", "flow", "flight"], "fl")])
def test_answer(strs, expected):
    assert Solution().longestCommonPrefix(strs) == expected
