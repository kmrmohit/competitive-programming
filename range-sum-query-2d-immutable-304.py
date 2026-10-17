'''
Day 9
1 attempt
'''
class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        m = len(matrix)
        n = len(matrix[0])
        self.prefixRowSumArray = [[0 for i in range(n+1)] for j in range(m+1)]
        for i in range(m):
            prefSum = 0
            for j in range(n):
                prefSum += matrix[i][j]
                self.prefixRowSumArray[i+1][j+1] = self.prefixRowSumArray[i][j+1] + prefSum

        # print(self.prefixColSumArray)
        # print(self.prefixRowSumArray)
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        result = self.prefixRowSumArray[max(row1,row2)+1][max(col1,col2)+1] - self.prefixRowSumArray[min(row1,row2)][max(col1,col2)+1] - self.prefixRowSumArray[max(row1,row2)+1][min(col1,col2)] + self.prefixRowSumArray[min(row1,row2)][min(col1,col2)]
        return result


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)