"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        curr = head
        while curr:
            _next = curr.next
            copy = Node(curr.val, _next, curr.random)
            curr.next = copy
            if curr.next and curr.next.next:
                curr = curr.next.next
            else:
                break
        curr = head.next
        while curr:
            curr.random = curr.random.next if curr.random else None
            if curr.next and curr.next.next:
                curr = curr.next.next
            else:
                break
        head = head.next
        curr = head
        while curr and curr.next:
            curr.next = curr.next.next
            curr = curr.next
        return head