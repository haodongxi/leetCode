from typing import List
from functools import reduce

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.sums = []
        for i in range(0,len(matrix)):
            sub_sum = []
            for j in range(0,len(matrix[i])):
                sub_sum.append( reduce(lambda x,y:x+y,matrix[i][0:j+1]))
            self.sums.append(sub_sum)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0
        for i in range(row1,row2+1):
            sum += (self.sums[i][col2] -  (0 if col1 == 0 else self.sums[i][col1-1]))
        return sum

if __name__ == '__main__':
    s = NumMatrix([[-1]])
    res = s.sumRegion(0,0,0,0)
    print(res)