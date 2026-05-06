# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(-1)
        node = head
        while list1 != None and list2 != None:
            v1 = list1.val
            v2 = list2.val
            if v1 == v2:
                list1_next = list1.next
                list2_next = list2.next
                list1.next = None
                list2.next = None
                node.next = list1
                node = node.next
                node.next = list2
                node = node.next
                list1 = list1_next
                list2 = list2_next
            elif v1 < v2:
                list1_next = list1.next
                list1.next = None
                node.next = list1
                node = node.next
                list1 = list1_next
            else:
                list2_next = list2.next
                list2.next = None
                node.next = list2
                node = node.next
                list2 = list2_next
        
        while list1 != None:
            list1_next = list1.next
            list1.next = None
            node.next = list1
            node = node.next
            list1 = list1_next

        while list2 != None:
            list2_next = list2.next
            list2.next = None
            node.next = list2
            node = node.next
            list2 = list2_next

        return head.next