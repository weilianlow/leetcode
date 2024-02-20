# https://leetcode.com/problems/rotate-array/
import pytest


class Solution(object):
    def rotate(self, nums, k):
        l = len(nums) - k % len(nums)
        nums[:] = nums[l:] + nums[:l]


@pytest.mark.parametrize("nums, k, expected", [
    ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4])])
def test_answer(nums, k, expected):
    Solution().rotate(nums, k)
    assert nums == expected
