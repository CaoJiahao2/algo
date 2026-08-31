from dsa.binary_tree.binary_tree_inorder_traversal.solution import Solution, TreeNode

def test_inorder():
    root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    assert Solution().inorderTraversal(root) == [1, 3, 2]

def test_inorder_empty():
    assert Solution().inorderTraversal(None) == []

