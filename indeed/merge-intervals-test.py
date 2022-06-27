import pytest


class Solution(object):
    def merge(self, intervals):
        if len(intervals) == 0:
            return []
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        res = [sorted_intervals[0]]
        for interval in sorted_intervals[1:]:
            # the next node's smallest value is smaller than the prev node's largest value, then overlapping
            if interval[0] <= res[-1][1]:
                # left boundary is the largest value
                res[-1][1] = max(interval[1], res[-1][1])
            else:
                res.append(interval)
        return res


@pytest.mark.parametrize("intervals, expected", [
    ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
    ([[1, 4], [4, 5]], [[1, 5]])])
def test_answer(intervals, expected):
    assert sorted(Solution().merge(intervals)) == sorted(expected)
