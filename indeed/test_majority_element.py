import pytest

"""
https://algodaily.com/challenges/majority-element
Suppose we're given an array of numbers like the following:
[4, 2, 4]
Could you find the majority element? A majority is defined as "the greater part, or more than half, of the total. It is a subset of a set consisting of more than half of the set's elements."
Let's assume that the array length is always at least one, and that there's always a majority element.
In the example above, the majority element would be 4.
"""


class Solution(object):
    def majorityElement(self, lst):
        dct = dict()
        for num in lst:
            if dct.get(num, None):
                dct[num] += 1
            else:
                dct[num] = 1

        lst = sorted(dct.items(), key=lambda x: x[1], reverse=True)
        return not lst[0][1] == lst[1][1]


@pytest.mark.parametrize("lst, expected", [
    ([4, 2, 4], True), ([4, 2, 4, 2], False)])
def test_answer(lst, expected):
    assert Solution().majorityElement(lst) == expected
