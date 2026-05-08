# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        def dfs(tree, _min = float("-inf")):
            if not tree:
                return
            nonlocal ans
            if tree.val >= _min:
                ans += 1
                _min = tree.val
            dfs(tree.left, _min)
            dfs(tree.right, _min)
        dfs(root)
        return ans