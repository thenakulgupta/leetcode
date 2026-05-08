# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        def postorder(tree, arr):
            if not tree:
                return []
            postorder(tree.left, arr)
            postorder(tree.right, arr)
            arr.append(tree.val)
        postorder(root, arr)
        return arr