# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSmallest(self, tree):
        while tree and tree.left:
            tree = tree.left
        return tree

    def search(self, key, tree):
        if not tree:
            return -1
        if key == tree.val:
            return tree
        if key < tree.val:
            return self.search(key, tree.left)
        if key > tree.val:
            return self.search(key, tree.right)

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.right and not root.left:
                return None
            elif root.right and not root.left:
                return root.right
            elif root.left and not root.right:
                return root.left
            else:
                smallest = self.findSmallest(root.right)
                root.val = smallest.val
                root.right = self.deleteNode(root.right, smallest.val)
        return root