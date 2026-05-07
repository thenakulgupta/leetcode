# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(-1)
        currAns = ans
        carry = 0
        while l1 or l2 or carry:
            _sum = carry
            carry = 0
            if l1:
                _sum += l1.val
                l1 = l1.next
            if l2:
                _sum += l2.val
                l2 = l2.next
            num = _sum%10
            carry = _sum//10
            currAns.next = ListNode(num)
            currAns = currAns.next
        return ans.next