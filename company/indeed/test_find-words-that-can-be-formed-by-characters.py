import pytest
from collections import defaultdict


class Solution(object):
    def countCharacters(self, words, chars):
        dct = defaultdict(int)
        for c in chars:
            dct[c] += 1
        count = 0
        for word in words:
            tmp_dct = dct.copy()
            tmp_count = 0
            for w in word:
                if tmp_dct.get(w, -1) <= 0:
                    tmp_count = 0
                    break
                else:
                    tmp_dct[w] -= 1
                    tmp_count += 1
            count += tmp_count
        return count


@pytest.mark.parametrize("words, chars, expected", [
    (["cat", "bt", "hat", "tree"], "atach", 6),
    (["hello", "world", "leetcode"], "welldonehoneyr", 10)])
def test_answer(words, chars, expected):
    assert Solution().countCharacters(words, chars) == expected
