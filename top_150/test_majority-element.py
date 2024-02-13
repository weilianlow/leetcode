# https://leetcode.com/problems/majority-element/
import pytest


class Solution(object):
    def majorityElement(self, nums):
        dct = dict()
        half = int(len(nums) / 2)
        ans = 0
        for v in nums:
            if dct.get(v, 0):
                dct[v] += 1
            else:
                dct[v] = 1
        half = int(len(nums) / 2)
        for k, v in dct.items():
            if v > half:
                return k
        return 0


@pytest.mark.parametrize("nums, expected", [
    ([3, 2, 3], 3)])
def test_answer(nums, expected):
    assert Solution().majorityElement(nums) == expected
