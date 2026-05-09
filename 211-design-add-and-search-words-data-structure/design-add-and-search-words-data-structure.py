class Node:
    def __init__(self):
        self.chars = {}
        self.eow = False

class WordDictionary:

    def __init__(self):
        self.head = Node()
        

    def addWord(self, word: str) -> None:
        curr = self.head
        for c in word:
            if c not in curr.chars:
                curr.chars[c] = Node()
            curr = curr.chars[c]
        curr.eow = True
        

    def search(self, word: str) -> bool:
        def dfsSearch(word, i = 0, curr = self.head):
            if i >= len(word):
                return curr.eow
            
            char = word[i]
            if char == ".":
                for _char in curr.chars:
                    if dfsSearch(word, i + 1, curr.chars[_char]):
                        return True
                return False
            else:
                if char not in curr.chars:
                    return False
                return dfsSearch(word, i + 1, curr.chars[char])

        return dfsSearch(word)



        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)