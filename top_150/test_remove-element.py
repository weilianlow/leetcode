# https://leetcode.com/problems/remove-element/submissions/
import pytest


class Solution:
    def removeElement(self, nums, val):
        nums[:] = [v for v in nums if v != val]


@pytest.mark.parametrize("nums, val, expected", [
    ([3, 2, 2, 3], 3, [2, 2])])
def test_answer(nums, val, expected):
    Solution().removeElement(nums, val)
    assert nums == expected
