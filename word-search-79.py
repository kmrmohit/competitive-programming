'''
Day 5
6 attempts, 4wa, 1tle
'''
class Solution:
    visited = {}
    def search(self, board, i, j, wordPos, word):
        m = len(board)
        n = len(board[0])  
        # print(i,j,wordPos)
        if wordPos == len(word):
            return True
        
        if i<0 or i>=m or j<0 or j>=n or self.visited.get(i*n+j) or board[i][j] != word[wordPos]:
            return False
        

        self.visited[i*n+j] = True

        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        found = False
        for [dx,dy] in directions:
            x,y = i+dx,j+dy
            found |= self.search(board,x,y,wordPos+1,word)

        self.visited[i*n+j] = False
        return found

    def exist(self, board: list[list[str]], word: str) -> bool:
        # self.search(board,0,0,0,word)
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.visited = {}
                found = self.search(board, i,j,0,word)
                if found:
                    return True
        return False
        