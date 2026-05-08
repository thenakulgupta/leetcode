# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        low, high = min(p.val, q.val), max(p.val, q.val)
        while root:
            if root.val >= low and root.val <= high:
                return root
            elif root.val < low:
                root = root.right
            else:
                root = root.left
        return None