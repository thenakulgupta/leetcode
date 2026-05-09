# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans = 0
        def count(root):
            nonlocal ans
            if not root:
                return 0
            leftCount = max(0, count(root.left))
            rightCount = max(0, count(root.right))
            ans = max(ans, leftCount + rightCount)
            return 1 + max(leftCount, rightCount)
        count(root)
        return ans