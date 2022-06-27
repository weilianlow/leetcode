import pytest


class Solution(object):
    def countCharacters(self, words, chars):
        total = []
        for word in words:
            chars_arr = list(chars)
            match = True
            for c in word:
                try:
                    chars_arr.remove(c)
                except:
                    match = False
                    break
            if match:
                total.append(word)
        return len(''.join(total))


@pytest.mark.parametrize("words, chars, expected", [
    (["cat", "bt", "hat", "tree"], "atach", 6),
    (["hello", "world", "leetcode"], "welldonehoneyr", 10)])
def test_answer(words, chars, expected):
    assert Solution().countCharacters(words, chars) == expected
