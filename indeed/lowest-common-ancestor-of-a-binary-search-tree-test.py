import pytest
from bst import create_bst, find_node


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return None
        if root.val == p.val or root.val == q.val:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if right and left:
            return root
        return right or left


@pytest.mark.parametrize("root,p,q,expected", [
    ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 8, 6),
    ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 4, 2),
    ([2, 1], 2, 1, 2)])
def test_answer(root, p, q, expected):
    _root = create_bst(root)
    _p = find_node(_root, p)
    _q = find_node(_root, q)
    _expected = find_node(_root, expected)
    assert Solution().lowestCommonAncestor(_root, _p, _q) == _expected
