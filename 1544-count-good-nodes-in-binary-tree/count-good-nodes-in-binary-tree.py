# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        def help(tree, currMin):
            if not tree:
                return 0
            curr = 0
            if tree.val >= currMin.val:
                currMin = tree
                curr = 1 + help(tree.left, currMin) + help(tree.right, currMin)
            else:
                curr = help(tree.left, currMin) + help(tree.right, currMin)
            return curr
        return 1 + help(root.left, root) + help(root.right, root)