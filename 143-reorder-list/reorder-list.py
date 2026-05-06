# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        s = f = head
        while f and f.next:
            s = s.next
            f = f.next.next
        
        otherHalf = s.next
        s.next = None

        _reversed = None
        while otherHalf:
            _next = otherHalf.next
            otherHalf.next = _reversed
            _reversed = otherHalf
            otherHalf = _next

        s = head
        while s and s.next and _reversed:
            _next = s.next
            _reversed_next = _reversed.next
            _reversed.next = _next
            s.next = _reversed
            _reversed = _reversed_next
            s = s.next.next