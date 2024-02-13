# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
import pytest


class Solution(object):
    def removeDuplicates(self, nums):
        tmp = list()
        for v in nums:
            if v not in tmp:
                tmp.append(v)
        nums[:] = tmp[:]


@pytest.mark.parametrize("nums, expected", [
    ([1, 1, 2], [1, 2])])
def test_answer(nums, expected):
    Solution().removeDuplicates(nums)
    assert nums == expected
