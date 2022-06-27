from collections import defaultdict
import pytest


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph = defaultdict(list)
        for p in prerequisites:
            graph[p[0]].append(p[1])
        visit = [0 for i in range(numCourses)]

        def dfs(v):
            if visit[v] == 1:
                return False
            if visit[v] == 2:
                return True
            visit[v] = 1
            for n in graph[v]:
                if not dfs(n): return False
            visit[v] = 2
            return True

        for v in range(numCourses):
            if not dfs(v): return False
        return True


@pytest.mark.parametrize("numCourses, prerequisites, expected", [
    (2, [[1, 0]], True),
    (2, [[1, 0], [0, 1]], False)])
def test_answer(numCourses, prerequisites, expected):
    assert Solution().canFinish(numCourses, prerequisites) == expected
