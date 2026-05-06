# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        i, n, ans = 0, 0, 0
        slow, fast, otherNodes = head, head, None

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        otherHalf = slow.next
        
        while otherHalf:
            _node = otherHalf
            _next = otherHalf.next
            _node.next = otherNodes
            otherNodes = _node
            otherHalf = _next

        while head and otherNodes:
            ans = max(ans, head.val + otherNodes.val)
            head = head.next
            otherNodes = otherNodes.next

        return ans