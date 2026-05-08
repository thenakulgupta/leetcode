# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        def bfs(tree):
            ans = []
            queue = deque([tree])
            while queue:
                temp = []
                for _ in range(len(queue)):
                    first = queue.popleft()
                    temp.append(first.val)
                    if first.left:
                        queue.append(first.left)
                    if first.right:
                        queue.append(first.right)
                ans.append(temp[-1])
            return ans
                
        return bfs(root)