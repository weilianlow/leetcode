import pytest


class Solution(object):
    def isValidSudoku(self, board):
        # horizontal/vertical check
        for i in range(9):
            uRow = {}
            uColumn = {}
            for j in range(9):
                if not uRow.get(board[i][j]):
                    if board[i][j] != '.':
                        uRow[board[i][j]] = True
                else:
                    return False
                if not uColumn.get(board[j][i]):
                    if board[j][i] != '.':
                        uColumn[board[j][i]] = True
                else:
                    return False
        # box check
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                val = self.isValidBox(board, i, j)
                if val is False:
                    return False
        return True

    def isValidBox(self, board, row, col):
        dct = {}
        for i in range(row, row + 3):
            for j in range(col, col + 3):
                if not dct.get(board[i][j]):
                    if board[i][j] != '.':
                        dct[board[i][j]] = True
                else:
                    return False
        return True


@pytest.mark.parametrize("board, expected", [
    ([["5", "3", ".", ".", "7", ".", ".", ".", "."]
         , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
         , [".", "9", "8", ".", ".", ".", ".", "6", "."]
         , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
         , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
         , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
         , [".", "6", ".", ".", ".", ".", "2", "8", "."]
         , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
         , [".", ".", ".", ".", "8", ".", ".", "7", "9"]], True),
    ([["8", "3", ".", ".", "7", ".", ".", ".", "."]
         , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
         , [".", "9", "8", ".", ".", ".", ".", "6", "."]
         , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
         , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
         , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
         , [".", "6", ".", ".", ".", ".", "2", "8", "."]
         , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
         , [".", ".", ".", ".", "8", ".", ".", "7", "9"]], False)])
def test_answer(board, expected):
    assert Solution().isValidSudoku(board) is expected
