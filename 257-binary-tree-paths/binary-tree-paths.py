# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.retArr = []
        def binaryTreePathsHelper(tree, arr=[]):
            if not tree:
                return

            arr.append(str(tree.val))
            if not tree.left and not tree.right:
                self.retArr.append("->".join(arr))
                arr.pop()
                return

            binaryTreePathsHelper(tree.left, arr)
            binaryTreePathsHelper(tree.right, arr)
            arr.pop()

        binaryTreePathsHelper(root)
        return self.retArr