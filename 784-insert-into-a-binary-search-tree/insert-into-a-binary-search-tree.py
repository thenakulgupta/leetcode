# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def add(self, val, tree):
        if not tree:
            return TreeNode(val)
        if val < tree.val:
            tree.left = self.add(val, tree.left)
        if val > tree.val:
            tree.right = self.add(val, tree.right)
        return tree

    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return self.add(val, root)