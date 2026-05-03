class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.head = None
        self.last = None
        self.ll_by_key = {}
        self.capacity = capacity


    def prependToLL(self, data):
        new_node = Node(data)
        self.removeFromLL(data[0])
        if self.head is None:
            self.ll_by_key[data[0]] = new_node
            self.head = new_node
            self.last = new_node
            return
        if len(self.ll_by_key.keys()) >= self.capacity:
            last = self.last
            last_second = last.prev if last and last.prev else None
            if(last_second):
                if last.data[0] in self.ll_by_key:
                    del self.ll_by_key[last.data[0]]
                last_second.next = None
                self.last = last_second
            else:
                self.head = None
                self.last = None
                self.ll_by_key = {}
        self.ll_by_key[data[0]] = new_node
        first = self.head
        self.head = new_node
        self.head.next = first
        if first:
            first.prev = new_node
            if len(self.ll_by_key.keys()) == 2:
                self.last = first


    def removeFromLL(self, key):
        node = self.ll_by_key[key] if key in self.ll_by_key else None
        if node:
            prev = node.prev
            if prev:
                prev.next = node.next
                if node.next:
                    node.next.prev = prev
                else:
                    self.last = prev
            else:
                _next = self.head.next if self.head else None
                if _next:
                    _next.prev = None
                self.head = _next
            del self.ll_by_key[key]
            if len(self.ll_by_key.keys()) <= 1:
                self.last = self.head


    def get(self, key: int) -> int:
        value = self.ll_by_key[key] if key in self.ll_by_key else None
        if not value:
            return -1
        self.prependToLL([key, value.data[1]])
        return value.data[1]

    def put(self, key: int, value: int) -> None:
        _value = self.ll_by_key[key] if key in self.ll_by_key else None
        self.prependToLL([key, value])


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)