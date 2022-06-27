import pytest


class Solution:
    def checkValid(self, matrix):
        size = len(matrix)
        for i in range(size):
            row = [v for v in range(1, size + 1)]
            col = [v for v in range(1, size + 1)]
            for j in range(size):
                try:
                    row.remove(matrix[i][j])
                except:
                    pass
                try:
                    col.remove(matrix[j][i])
                except:
                    pass
            if len(row) + len(col) > 0:
                return False
        return True


@pytest.mark.parametrize("matrix, expected", [
    ([[1, 2, 3], [3, 1, 2], [2, 3, 1]], True),
    ([[1, 1, 1], [1, 2, 3], [1, 2, 3]], False)])
def test_answer(matrix, expected):
    assert Solution().checkValid(matrix) == expected
