from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0, 9):
            if listContainLikeSymbol(board[i]) == False:
                return False
            tempColumList = []
            for j in range(0,9):
                tempColumList.append(board[j][i])
            if listContainLikeSymbol(tempColumList)==False:
                return False
            row = i//3*3
            colum = i%3*3
            tempFGList = []
            for j in range(0,3):
                 for k in range(0,3):
                    tempFGList.append(board[row+j][colum+k])
            if listContainLikeSymbol(tempFGList)==False:
                return False
        return True
def listContainLikeSymbol(nums):
    dotCount = nums.count('.')
    numsCount = len(nums) - dotCount
    numDict = {}
    for a in nums:
        numDict[a] = ""
    del numDict['.']
    countInDict = len(numDict.keys())
    return True if numsCount == countInDict else False


if __name__ == "__main__":
    s = Solution()
    # s.isValidSudoku()
