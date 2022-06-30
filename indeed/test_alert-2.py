'''
We are working on a security system for a badged-access room in our company's building.
Given an ordered list of employees who used their badge to enter or exit the room, write a function that returns two collections:
# 1. All employees who didn't use their badge while exiting the room - they recorded an enter without a matching exit. (All employees are required to leave the room before the log ends.)
# 2. All employees who didn't use their badge while entering the room - they recorded an exit without a matching enter. (The room is empty when the log begins.)
Each collection should contain no duplicates, regardless of how many times a given employee matches the criteria for belonging to it

'''
from collections import defaultdict
import pytest


class Solution():
    def alertNames(self, badge_records):
        # create dict
        dct = defaultdict(list)
        for rec in badge_records:
            dct[rec[0]].append(rec[1])
        #
        no_exit_dct, no_enter_dct = [], []
        for employee in dct:
            entries = dct[employee]
            # first and last record check
            if entries[0] == 'exit':
                no_enter_dct.append(employee)
            if entries[-1] == 'enter':
                no_exit_dct.append(employee)
            # in between
            for i, _ in enumerate(entries):
                if i > 0:
                    if entries[i] == entries[i - 1]:
                        if entries[i - 1] == 'enter':
                            if employee not in no_exit_dct:
                                no_exit_dct.append(employee)
                        else:
                            if employee not in no_enter_dct:
                                no_enter_dct.append(employee)
        return [sorted(no_exit_dct), sorted(no_enter_dct)]


@pytest.mark.parametrize("badge_records, expected", [
    ([["Martha", "exit"], ["Paul", "enter"], ["Martha", "enter"], ["Martha", "exit"], ["Jennifer", "enter"],
      ["Paul", "enter"], ["Curtis", "exit"], ["Curtis", "enter"], ["Paul", "exit"], ["Martha", "enter"],
      ["Martha", "exit"], ["Jennifer", "exit"], ["Paul", "enter"], ["Paul", "enter"], ["Martha", "exit"]],
        [["Curtis", "Paul"], ["Martha", "Curtis"]]),
    ([["Paul", "enter"], ["Paul", "enter"], ["Paul", "exit"]], [["Paul"], []]),
    ([["Paul", "enter"], ["Paul", "exit"], ["Paul", "exit"]], [[], ["Paul"]]),
    ([["Paul", "enter"], ["Paul", "exit"], ["Paul", "exit"], ["Paul", "enter"], ["Martha", "enter"],["Martha", "exit"]],
        [["Paul"], ["Paul"]]),
    ([["Paul", "enter"], ["Paul", "exit"]], [[], []]),
    ([["Paul", "enter"], ["Paul", "enter"], ["Paul", "exit"], ["Paul", "exit"]], [["Paul"], ["Paul"]]),
    ([["Paul", "enter"], ["Paul", "exit"], ["Paul", "exit"], ["Paul", "enter"]], [["Paul"], ["Paul"]])
])
def test_answer(badge_records, expected):
    assert Solution().alertNames(badge_records) == [sorted(expected[0]), sorted(expected[1])]
