'''
Day 10
1 attempt
'''
class TrieNode:
    def __init__(self):
        self.word = None
        self.children = {}

class Trie:
    def __init__(self):
        self.treeRoot = TrieNode()
    
    def insert(self, word):
        node = self.treeRoot
        for char in word:
            node = node.children.setdefault(char, TrieNode())
        node.word = word

class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        prefixTree = Trie()
        for word in words:
            prefixTree.insert(word)

        visited = {}

        def isValidPos(x:int, y:int) -> bool:
            return x>=0 and x<len(board) and y>=0 and y<len(board[0]) and not visited.get((x,y))
    
        answerSet = []
        dirs = [[0,1],[1,0],[-1,0],[0,-1]]

        def searchMatrix(posX: int, posY: int, treeNode: TrieNode | None) -> None:
            if not treeNode:
                return
            if treeNode.word:
                answerSet.append(treeNode.word)
                treeNode.word = None
            
            visited[(posX,posY)] = True
            for [dx, dy] in dirs:
                newPosX, newPosY = posX+dx, posY+dy
                if isValidPos(newPosX,newPosY) and treeNode.children.get(board[newPosX][newPosY]):
                    searchMatrix(newPosX, newPosY, treeNode.children.get(board[newPosX][newPosY]))
            
            visited[(posX,posY)] = False

        for i in range(len(board)):
            for j in range(len(board[0])):
                visited.clear()
                if prefixTree.treeRoot.children.get(board[i][j]):
                    searchMatrix(i,j,prefixTree.treeRoot.children.get(board[i][j]))

        return answerSet
