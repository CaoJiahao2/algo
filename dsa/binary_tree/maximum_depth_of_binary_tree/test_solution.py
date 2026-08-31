from dsa.binary_tree.maximum_depth_of_binary_tree.solution import Solution, TreeNode

def test_max_depth():
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert Solution().maxDepth(root) == 3

def test_max_depth_empty():
    assert Solution().maxDepth(None) == 0

