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

        def pathSumBacktrack(tree, targetSum, currentSum=0):
            if not tree:
                return False

            currentSum += tree.val
                
            if targetSum == currentSum and not tree.left and not tree.right:
                return True

            leftSum = pathSumBacktrack(tree.left, targetSum, currentSum)
            rightSum = pathSumBacktrack(tree.right, targetSum, currentSum)
            return leftSum or rightSum
        
        return pathSumBacktrack(root, targetSum)