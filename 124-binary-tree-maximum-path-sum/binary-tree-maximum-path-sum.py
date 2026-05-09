# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = -inf
        def _sum(tree):
            if not tree:
                return 0
            nonlocal ans
            leftSum = max(0, _sum(tree.left))
            rightSum = max(0, _sum(tree.right))
            ans = max(ans, tree.val + leftSum + rightSum)
            return tree.val + max(leftSum, rightSum)
        _sum(root)
        return ans