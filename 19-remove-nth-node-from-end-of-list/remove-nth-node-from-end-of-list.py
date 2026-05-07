# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = 0
        curr = head
        prevNode = None
        while curr:
            curr = curr.next
            i += 1
            if i > n:
                prevNode = prevNode.next if prevNode else head
        if prevNode:
            prevNodeNext = prevNode.next
            if prevNodeNext and prevNodeNext.next:
                prevNode.next = prevNodeNext.next
            else:
                prevNode.next = None
            del prevNodeNext
        else:
            if head.next == None:
                head = None
            else: head = head.next
        return head