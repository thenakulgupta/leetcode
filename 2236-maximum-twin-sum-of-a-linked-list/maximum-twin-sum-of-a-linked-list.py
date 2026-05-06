# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        ans = 0
        slow, fast = head, head
        arr = [slow.val]

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            arr.append(slow.val)

        slow = slow.next

        for i in range(len(arr) - 1, -1, -1):
            ans = max(ans, arr[i] + slow.val)
            slow = slow.next

        return ans