# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, tree1, tree2):
        if not tree1 and not tree2:
            return True
        if not tree1 or not tree2:
            return False
        isMatch = tree1.val == tree2.val
        if not isMatch:
            return False
        return self.isSameTree(tree1.left, tree2.left) and self.isSameTree(tree1.right, tree2.right)


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not subRoot:
            return True
        isMatch = self.isSameTree(root, subRoot)
        if isMatch:
            return True
        isLIdentical = self.isSubtree(root.left, subRoot)
        isRIdentical = self.isSubtree(root.right, subRoot)
        return isLIdentical or isRIdentical