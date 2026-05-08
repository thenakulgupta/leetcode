# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(tree, seq):
            if not tree:
                return []
            inorder(tree.left, seq)
            seq.append(tree.val)
            inorder(tree.right, seq)
        seq = []
        inorder(root, seq)
        return seq[k - 1]