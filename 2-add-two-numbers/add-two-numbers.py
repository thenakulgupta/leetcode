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
        while l1 and l2:
            _sum = l1.val + l2.val + carry
            carry = 0
            if _sum > 9:
                carry = 1
                _sum -= 10
            currAns.next = ListNode(_sum)
            currAns = currAns.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            _sum = l1.val + carry
            carry = 0
            if _sum > 9:
                carry = 1
                _sum -= 10
            currAns.next = ListNode(_sum)
            currAns = currAns.next
            l1 = l1.next
        while l2:
            _sum = l2.val + carry
            carry = 0
            if _sum > 9:
                carry = 1
                _sum -= 10
            currAns.next = ListNode(_sum)
            currAns = currAns.next
            l2 = l2.next
        if carry == 1:
            currAns.next = ListNode(carry)
            currAns = currAns.next
        return ans.next