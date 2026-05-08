# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])

        curr = preorder[0]
        preorder = preorder[1:]
        currInorder = inorder.index(curr)
        preorderLeft = preorder[ : currInorder]
        preorderRight = preorder[currInorder : ]
        inorderLeft = inorder[ : currInorder]
        inorderRight = inorder[currInorder + 1 : ]

        root = TreeNode(curr)
        root.left = self.buildTree(preorderLeft, inorderLeft)
        root.right = self.buildTree(preorderRight, inorderRight)
        return root