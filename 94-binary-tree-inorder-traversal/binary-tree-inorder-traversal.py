# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        arr = []
        left = self.inorderTraversal(root.left)
        right = self.inorderTraversal(root.right)
        for n in left:
            arr.append(n)
        arr.append(root.val)
        for n in right:
            arr.append(n)
        return arr