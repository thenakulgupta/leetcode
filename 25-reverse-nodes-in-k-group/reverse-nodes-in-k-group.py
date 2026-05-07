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
        last = None
        _head = None
        isFirstTime = True
        while curr:
            main = None
            i = 0
            _last = curr
            while curr and i < k:
                nxt = curr.next
                curr.next = main
                main = curr
                curr = nxt
                i += 1
            if i != k:
                curr = main
                main = None
                i = 0
                while curr and i < k:
                    nxt = curr.next
                    curr.next = main
                    main = curr
                    curr = nxt
                    i += 1
            if isFirstTime:
                _head = main
                isFirstTime = False
            if last:
                # print("_last", _last.val, _last.next)
                last.next = main if i == k else _last
            last = _last
            if i != k:
                break
            # print(curr.val)
        return _head