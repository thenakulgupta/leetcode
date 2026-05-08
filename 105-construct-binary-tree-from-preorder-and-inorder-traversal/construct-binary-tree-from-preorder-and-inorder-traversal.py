# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def build(self, preL, preR, inL, inR, preorder, inorder, hm):
        if preL > preR or inL > inR:
            return None

        rootVal = preorder[preL]
        root = TreeNode(rootVal)
        inOrderIndex = hm[rootVal]
        leftSize = inOrderIndex - inL

        root.left = self.build(preL + 1, preL + leftSize, inL, inOrderIndex - 1, preorder, inorder, hm)
        root.right = self.build(preL + leftSize + 1, preR, inOrderIndex + 1, inR, preorder, inorder, hm)
        return root
        
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hm = {}
        n = len(inorder)
        for i in range(n):
            hm[inorder[i]] = i
        return self.build(0, n - 1, 0, n - 1, preorder, inorder, hm)