# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(tree, low = float("-inf"), high = float("inf")):
            if not tree:
                return True
            if tree.val <= low or tree.val >= high:
                return False
            return validate(tree.left, low, tree.val) and validate(tree.right, tree.val, high)
        return validate(root)