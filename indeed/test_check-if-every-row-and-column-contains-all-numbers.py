import pytest


class Solution:
    def checkValid(self, matrix):
        size = len(matrix)
        for i in range(size):
            row_dct, col_dct = {}, {}
            for j in range(size):
                val = matrix[i][j]
                if not row_dct.get(val, False):
                    row_dct[val] = True
                else:
                    return False
                val = matrix[j][i]
                if not col_dct.get(val, False):
                    col_dct[val] = True
                else:
                    return False
        return True


@pytest.mark.parametrize("matrix, expected", [
    ([[1, 2, 3], [3, 1, 2], [2, 3, 1]], True),
    ([[1, 1, 1], [1, 2, 3], [1, 2, 3]], False)])
def test_answer(matrix, expected):
    assert Solution().checkValid(matrix) == expected
