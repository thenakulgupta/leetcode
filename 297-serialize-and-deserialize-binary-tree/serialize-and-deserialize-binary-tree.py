# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return ""
        arr_preorder = []
        def preorder(tree, arr):
            if not tree:
                arr.append("N")
                return
            arr.append(str(tree.val))
            preorder(tree.left, arr)
            preorder(tree.right, arr)
        preorder(root, arr_preorder)
        encrypted_preorder = "-----".join(arr_preorder)
        return encrypted_preorder
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None

        preorder_arr = data.split("-----")
        i = 0

        def makeTree():
            nonlocal i
            if i >= len(preorder_arr):
                return None
            
            if preorder_arr[i] == "N":
                i += 1
                return None
            tree = TreeNode(preorder_arr[i])
            i += 1
            tree.left = makeTree()
            tree.right = makeTree()
            return tree

        return makeTree()

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))