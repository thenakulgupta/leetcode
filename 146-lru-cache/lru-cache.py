class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache_count = 0
        self.cache_head = None
        self.cache_tail = None
        self.cache_hm = {}

    def printCache(self, val):
        # node = self.cache_head
        # print(val, " ", end="")
        # while node:
        #     print(node.val, "-> ", end="")
        #     node = node.next
        # print()
        pass
        

    def get(self, key: int) -> int:
        self.printCache("get")
        node = self.cache_hm[key] if key in self.cache_hm else None
        if node:
            self.remove(key)
            self.insert(key, node.val)
        self.printCache("get1")
        return node.val if node else -1


    def put(self, key: int, value: int) -> None:
        self.printCache("put")
        if self.cache_count >= self.capacity and key not in self.cache_hm:
            self.remove_last()
        else:
            self.remove(key)
        self.insert(key, value)
        self.printCache("put1")


    def insert(self, key, val):
        self.printCache("insert")
        new_cache = Node(key, val)
        node = self.cache_head
        self.cache_head = new_cache
        new_cache.next = node
        if new_cache.next:
            new_cache.next.prev = new_cache
        if not node:
            self.cache_tail = new_cache
        self.cache_hm[key] = new_cache
        self.cache_count += 1


    def remove(self, key):
        self.printCache("remove")
        if key not in self.cache_hm:
            return

        node = self.cache_hm[key]
        prev = node.prev
        _next = node.next
        if prev:
            prev.next = _next
        else:
            self.cache_head = _next
        if _next:
            _next.prev = prev
        else:
            self.cache_tail = prev
        if not prev and not _next:
            self.cache_head = None
            self.cache_tail = None
        del node
        del self.cache_hm[key]
        self.cache_count -= 1


    def remove_last(self):
        self.printCache("remove_last")
        node = self.cache_tail
        if not node:
            return
        prev = node.prev
        if prev:
            self.cache_tail = prev
            prev.next = None
        else:
            self.cache_head = None
            self.cache_tail = None

        self.cache_count -= 1
        key = node.key
        del self.cache_hm[key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)