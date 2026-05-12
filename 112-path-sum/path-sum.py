# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        def helper(tree, targetSum, currentSum = 0):
            if not tree:
                return False

            currentSum += tree.val
            if not tree.left and not tree.right:
                return currentSum == targetSum

            leftSum = helper(tree.left, targetSum, currentSum)
            rightSum = helper(tree.right, targetSum, currentSum)

            return leftSum or rightSum

        return helper(root, targetSum)