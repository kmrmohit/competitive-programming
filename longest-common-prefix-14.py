'''
Day 10
1 attempt
'''
class TrieNode:
    def __init__(self):
        self.nodecount = 0
        self.children = {}

class Trie:
    def __init__(self):
        self.treeRoot = TrieNode()
        self.wordsCount = 0
        self.longestPrefix = ""

    def insert(self, word):
        self.wordsCount += 1
        self.longestPrefix = ""
        longestCommonPos = None
        node = self.treeRoot
        for index, char in enumerate(word):
            node = node.children.setdefault(char, TrieNode())
            node.nodecount += 1
            if node.nodecount == self.wordsCount:
                longestCommonPos = index + 1
        self.longestPrefix = word[:longestCommonPos] if longestCommonPos else ""

    def getLongestPrefix(self) -> str:
        return self.longestPrefix

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefixTree = Trie()
        for word in strs:
            prefixTree.insert(word)
        return prefixTree.getLongestPrefix()