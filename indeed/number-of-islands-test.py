import pytest


class Solution(object):
    def numIslands(self, grid):
        self.score = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    self.helper(grid, i, j)
                    self.score += 1
        return self.score

    def helper(self, grid, i, j):
        # mark current cell as visited
        grid[i][j] = '-1'
        # traveral
        if (j - 1) >= 0 and grid[i][j - 1] == '1':
            self.helper(grid, i, j - 1)
        if (j + 1) < len(grid[i]) and grid[i][j + 1] == '1':
            self.helper(grid, i, j + 1)
        if (i - 1) >= 0 and grid[i - 1][j] == '1':
            self.helper(grid, i - 1, j)
        if (i + 1) < len(grid) and grid[i + 1][j] == '1':
            self.helper(grid, i + 1, j)


@pytest.mark.parametrize("grid, expected", [
    ([["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]], 3),
    ([["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]], 1)])
def test_answer(grid, expected):
    assert Solution().numIslands(grid) == expected
