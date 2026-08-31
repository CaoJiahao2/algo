from dsa.binary_tree.lowest_common_ancestor_of_binary_tree.solution import Solution, TreeNode

def test_lca():
    root = TreeNode(3)
    root.left = p = TreeNode(5)
    root.right = TreeNode(1)
    p.left = TreeNode(6)
    p.right = TreeNode(2)
    q = TreeNode(4)
    p.right.right = q
    assert Solution().lowestCommonAncestor(root, p, q) is p

