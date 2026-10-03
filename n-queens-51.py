'''
Day 5
1 attempt
'''
class Solution:
    def isSafe(self,n, queens):
        # same row, same column, any diagnoals
        for [x,y] in queens.values():
            for [i,j] in queens.values():
                if x==i and y==j:
                    continue
                if x==i or y==j:
                    return False
                absx,absy=abs(x-i),abs(y-j)
                if absx==absy:
                    return False
        return True

    def solveNQueens(self, n: int) -> list[list[str]]:
        possiblePlacements = []
        def solve(n, rowNo, queens):
            if rowNo==n:
                possiblePlacements.append(queens.copy())
                return
            
            if rowNo >= n:
                return
            
            for i in range(n):
                queens[rowNo*n+i] = [rowNo,i]
                if self.isSafe(n, queens):
                    solve(n, rowNo+1, queens)
                del queens[rowNo*n+i]
        
        solve(n, 0, {})
        result = []
        for placements in possiblePlacements:
            curr = [('.' * n) for i in range(n)]
            for [x,y] in placements.values():
                curr[x] = '.'*y + 'Q' + '.'*(n-y-1)
            result.append(curr)
        
        return result