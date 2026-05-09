class Node:
    def __init__(self):
        self.chars = [None] * 26
        self.eow = False

class Trie:

    def __init__(self):
        self.head = Node()

    def charToInt(self, s):
        return ord(s) - 97

    def insert(self, word: str) -> None:
        curr = self.head
        for i, w in enumerate(word):
            w = self.charToInt(w)
            if not curr.chars[w]:
                curr.chars[w] = Node()
            curr = curr.chars[w]
            if i == len(word) - 1:
                curr.eow = True
        

    def search(self, word: str) -> bool:
        curr = self.head
        for i, w in enumerate(word):
            w = self.charToInt(w)
            if not curr.chars[w]:
                return False
            curr = curr.chars[w]
            if i == len(word) - 1:
                return curr.eow
        return False
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.head
        for i, w in enumerate(prefix):
            w = self.charToInt(w)
            if not curr.chars[w]:
                return False
            curr = curr.chars[w]
            if i == len(prefix) - 1:
                return True
        return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)