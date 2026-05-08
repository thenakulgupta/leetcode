# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getHeight(self, tree):
        if not tree:
            return 0

        leftHeight = self.getHeight(tree.left)
        rightHeight = self.getHeight(tree.right)

        if leftHeight == -1 or rightHeight == -1:
            return -1

        if abs(leftHeight - rightHeight) <= 1:
            return 1 + max(leftHeight, rightHeight)
        else:
            return -1


    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        ans = self.getHeight(root)

        return ans != -1