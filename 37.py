from typing import List
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
    
        columAr = []
        fgArr = []
        for i in range(0,9):

            tempArr = []
            for j in range(0,9):
                tempArr.append(board[j][i])
            columAr.append(tempArr)

            tempFGList = []
            row = i//3*3
            colum = i%3*3
            for j in range(0,3):
                for k in range(0,3):
                    tempFGList.append(board[row+j][colum+k])
            fgArr.append(tempFGList)
        
                        

        
            

        

            
if __name__ == "__main__":
    s = Solution()
    s.solveSudoku([[1,2,3],[1,2,3],[1,2,3]])