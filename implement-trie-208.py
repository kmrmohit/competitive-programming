'''
Day 10
1 attempt
'''
class Trie:

    def __init__(self):
        self.prefixTree = [[0, None] for i in range(26)]

    def insert(self, word: str) -> None:
        node = self.prefixTree
        for index, c in enumerate(word):
            charIndex = ord(c) - ord('a')
            if not node[charIndex][1]:
                node[charIndex][1] = [[0, None] for i in range(26)]

            node[charIndex][0] += (1 if index == len(word)-1 else 0)
            node = node[charIndex][1]


    def search(self, word: str) -> bool:
        node = self.prefixTree
        for index, c in enumerate(word):
            charIndex = ord(c) - ord('a')
            if node[charIndex][1]:
                if index == len(word)-1 and node[charIndex][0] > 0:
                    return True
                node = node[charIndex][1]
            else:
                return False
        return False
 
    def startsWith(self, prefix: str) -> bool:
        node = self.prefixTree
        for c in prefix:
            charIndex = ord(c) - ord('a')
            if node[charIndex][1]:
                node = node[charIndex][1]
            else:
                return False
        return True        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)