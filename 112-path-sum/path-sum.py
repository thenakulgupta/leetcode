# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def helper(tree, targetSum, currentSum = 0):
            if not tree:
                return False

            currentSum += tree.val
            if currentSum == targetSum and not tree.left and not tree.right:
                return True

            leftSum = helper(tree.left, targetSum, currentSum)
            rightSum = helper(tree.right, targetSum, currentSum)

            return leftSum or rightSum

        return helper(root, targetSum)