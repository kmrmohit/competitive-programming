'''
Day 10
1 attempt
'''
class WordDictionary:

    def __init__(self):
        self.wordTree = [[0, None] for i in range(26)]

    def addWord(self, word: str) -> None:
        node = self.wordTree
        for index, c in enumerate(word):
            charIndex = ord(c) - ord('a')
            if node[charIndex][1] is None:
                node[charIndex][1] = [[0,None] for i in range(26)]
            node[charIndex][0] += (1 if index == len(word)-1 else 0)
            node = node[charIndex][1]

    def search(self, word: str) -> bool:
        def wordSearch(node, count: int, pos: int) -> bool:
            if pos == len(word):
                return True if count > 0 else False
            if not node:
                return False
            char = word[pos]
            if char != '.':
                charIndex = ord(char) - ord('a')
                return wordSearch(node[charIndex][1], node[charIndex][0], pos+1) if node[charIndex][1] else False
            else:
                exploreResult = False
                for charIndex in range(26):
                    if node[charIndex][1]:
                        exploreResult |= wordSearch(node[charIndex][1], node[charIndex][0], pos+1)
                return exploreResult

        return wordSearch(self.wordTree,0,0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)