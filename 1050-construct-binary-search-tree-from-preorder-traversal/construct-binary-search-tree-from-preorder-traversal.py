# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def add(self, p, tree):
        if not tree:
            return TreeNode(p)
        if p < tree.val:
            tree.left = self.add(p, tree.left)
        if p > tree.val:
            tree.right = self.add(p, tree.right)
        return tree

    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        tree = None
        for p in preorder:
            tree = self.add(p, tree)
        return tree