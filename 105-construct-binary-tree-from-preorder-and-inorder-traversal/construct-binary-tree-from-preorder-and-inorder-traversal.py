# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def build(self, preorder, preL, preR, inorder, inL, inR, hm):
        if preL > preR or inL > inR:
            return None

        rootVal = preorder[preL]
        root = TreeNode(rootVal)

        inorderIndex = hm[rootVal]

        leftSize = inorderIndex - inL

        root.left = self.build(
            preorder,
            preL + 1,
            preL + leftSize,
            inorder,
            inL,
            inorderIndex - 1,
            hm
        )

        root.right = self.build(
            preorder,
            preL + leftSize + 1,
            preR,
            inorder,
            inorderIndex + 1,
            inR,
            hm
        )

        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hm = {}

        for i, val in enumerate(inorder):
            hm[val] = i

        return self.build(
            preorder,
            0,
            len(preorder) - 1,
            inorder,
            0,
            len(inorder) - 1,
            hm
        )