from datetime import datetime
from collections import defaultdict

import pytest


class Solution:
    def alertNames(self, keyName, keyTime):
        dct = defaultdict(list)
        for i in range(len(keyName)):
            dct[keyName[i]].append(datetime.strptime(keyTime[i], '%H:%M'))

        result = []
        for key in sorted(dct):
            times = sorted(dct[key])
            prev = 0
            for i in range(len(times)):
                if i > 0:
                    cur = (times[i] - times[i - 1]).total_seconds() / 60
                    # check criteria
                    if 0 < prev <= 60 and 0 < cur <= 60 and (prev + cur) <= 60:
                        result.append(key)
                        break
                    # set cur to prev
                    prev = 0 if cur > 60 else cur
        return result


@pytest.mark.parametrize("keyName, keyTime, expected", [
    (["daniel", "daniel", "daniel", "luis", "luis", "luis", "luis"],
     ["10:00", "10:40", "11:00", "09:00", "11:00", "13:00", "15:00"], ["daniel"]),
    (["alice", "alice", "alice", "bob", "bob", "bob", "bob"],
     ["12:01", "12:00", "18:00", "21:00", "21:20", "21:30", "23:00"], ["bob"])])
def test_answer(keyName, keyTime, expected):
    assert Solution().alertNames(keyName, keyTime) == expected
