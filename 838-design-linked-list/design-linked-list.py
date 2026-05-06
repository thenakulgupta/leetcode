class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.dll = None
        self.count = 0

    def get(self, index: int) -> int:
        if index >= self.count:
            return -1

        currentCount = 0
        curr = self.dll
        while currentCount != index:
            curr = curr.next
            currentCount += 1
        return curr.val

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        if self.dll == None:
            self.dll = node
        else:
            curr = self.dll
            node.next = curr
            self.dll = node
        self.count += 1
        

    def addAtTail(self, val: int) -> None:
        node = Node(val)
        if self.dll == None:
            self.dll = node
        else:
            curr = self.dll
            while curr.next != None:
                curr = curr.next
            curr.next = node
        self.count += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.count:
            return
        if index == self.count:
            self.addAtTail(val)
            return

        node = Node(val)
        curr = self.dll

        self.count += 1

        if index == 0:
            self.dll = node
            self.dll.next = curr
            return

        currentCount = 0
        while currentCount != index - 1:
            curr = curr.next
            currentCount += 1
        _next = curr.next
        curr.next = node
        curr = curr.next
        curr.next = _next
        

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.count:
            return


        self.count -= 1

        if self.count == 0:
            del self.dll
            self.dll = None
            return

        if index == 0:
            curr = self.dll
            _next = curr.next
            self.dll = _next
            del curr
            return

        currentCount = 0
        curr = self.dll
        while currentCount != index - 1:
            curr = curr.next
            currentCount += 1
        _next = curr.next
        curr.next = curr.next.next
        del _next
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)