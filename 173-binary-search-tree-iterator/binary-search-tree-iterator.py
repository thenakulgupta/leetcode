# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def pushLeft(self, tree):
        while tree:
            self.stack.append(tree)
            tree = tree.left


    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.pushLeft(root)
        

    def next(self) -> int:
        ans = self.stack.pop()
        self.pushLeft(ans.right)
        return ans.val


    def hasNext(self) -> bool:
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()