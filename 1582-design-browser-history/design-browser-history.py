class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.dll = Node(homepage)
        self.curr = self.dll
        

    def visit(self, url: str) -> None:
        if self.curr.next:
            del self.curr.next
        curr = self.curr
        self.curr.next = Node(url)
        self.curr = self.curr.next
        self.curr.prev = curr
        

    def back(self, steps: int) -> str:
        i = 0
        while self.curr.prev != None and i != steps:
            self.curr = self.curr.prev
            i += 1
        return self.curr.val
        

    def forward(self, steps: int) -> str:
        i = 0
        while self.curr.next != None and i != steps:
            self.curr = self.curr.next
            i += 1
        return self.curr.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)