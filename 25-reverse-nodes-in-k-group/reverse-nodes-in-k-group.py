# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1 or not head.next:
            return head
        curr = head
        prev_group_tail = None
        new_head = None
        isFirstTime = True
        while curr:
            reversed_head = None
            i = 0
            group_tail = curr
            while curr and i < k:
                nxt = curr.next
                curr.next = reversed_head
                reversed_head = curr
                curr = nxt
                i += 1
            if i != k:
                curr = reversed_head
                reversed_head = None
                i = 0
                while curr and i < k:
                    nxt = curr.next
                    curr.next = reversed_head
                    reversed_head = curr
                    curr = nxt
                    i += 1
            if isFirstTime:
                new_head = reversed_head
                isFirstTime = False
            if prev_group_tail:
                prev_group_tail.next = reversed_head if i == k else group_tail
            prev_group_tail = group_tail
            if i != k:
                break
        return new_head