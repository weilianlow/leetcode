# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
import pytest


class Solution(object):
    def removeDuplicates(self, nums):
        i = len(nums) - 1
        dct = dict()
        while i >= 0:
            count = dct.get(nums[i], 0)
            if count == 0:
                dct[nums[i]] = 1
            elif count >= 2:
                del nums[i]
            else:
                dct[nums[i]] += 1
            i -= 1


@pytest.mark.parametrize("nums, expected", [
    ([1, 1, 1, 2, 2, 3], [1, 1, 2, 2, 3])])
def test_answer(nums, expected):
    Solution().removeDuplicates(nums)
    assert nums == expected
