# https://leetcode.com/problems/find-first-palindromic-string-in-the-array/
import pytest


class Solution(object):
    def firstPalindrome(self, words):
        for word in words:
            mid = int(len(word) / 2)
            j = len(word) - 1
            isPalindromic = [word[i] == word[j - i] for i in range(int(len(word) / 2))]
            if all(isPalindromic):
                return word
        return ""


@pytest.mark.parametrize("words", [
    (["abc", "car", "ada", "racecar", "cool"])])
def test_answer(words):
    assert Solution().firstPalindrome(words)
