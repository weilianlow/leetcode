class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def create_bst(lst):
    childs, parents = [], []
    level = 0
    root = None
    while len(lst) > 0:
        # reset childs and parents
        if len(childs) > 0:
            parents = childs
        # create child node
        childs = []
        for i in range(2 ** level):
            if len(lst) > 0:

                if lst[0] is not None:
                    childs.append(TreeNode(lst[0]))
                else:
                    childs.append(TreeNode(None))
                # remove child from lst
                # print(f'level:{p}, element:{lst[0]}')
                lst = lst[1:]
        # link to parents
        if len(parents) > 0:
            for i, child in enumerate(childs):
                if parents[i // 2].left is None:
                    parents[i // 2].left = child
                elif parents[i // 2].right is None:
                    parents[i // 2].right = child
        else:
            root = childs[0]
        level += 1
    return root


def find_node(cur_node, target_val):
    if cur_node is None:
        return None
    if cur_node.val == target_val:
        return cur_node
    left = find_node(cur_node.left, target_val)
    if left is not None:
        return left
    right = find_node(cur_node.right, target_val)
    if right is not None:
        return right
