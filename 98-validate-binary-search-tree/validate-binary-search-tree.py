# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr = []
        def inorder(tree):
            if not tree:
                return []
            inorder(tree.left)
            arr.append(tree.val)
            inorder(tree.right)
        inorder(root)
        for i in range(1, len(arr)):
            if arr[i - 1] >= arr[i]:
                return False
        return True