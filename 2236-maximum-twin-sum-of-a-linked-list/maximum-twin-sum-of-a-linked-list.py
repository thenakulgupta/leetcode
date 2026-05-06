# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        i, n, ans = 0, 0, 0
        mid, otherNodes = None, None
        curr = head

        while curr:
            curr = curr.next
            n += 1

        curr = head

        while curr:
            if i < (n / 2) - 1:
                curr = curr.next
                i += 1
            elif i == (n / 2) - 1:
                mid = curr
                break
        
        otherHalf = mid.next
        mid.next = None

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