# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ans = ListNode(0)
        currAns = ans
        while True:
            minValue = float("inf")
            minValueI = -1
            for i in range(len(lists)):
                l = lists[i]
                if l and minValue > l.val:
                    minValue = l.val
                    minValueI = i
            if minValueI == -1:
                break
            currAns.next = lists[minValueI]
            currAns = currAns.next
            lists[minValueI] = lists[minValueI].next
        return ans.next