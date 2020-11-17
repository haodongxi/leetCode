class Solution:
    def convert(self, s: str, numRows: int) -> str:
        strNum = len(s)
        if strNum<=numRows:
            return "".join(s)
        if numRows == 1:
            return s
        oneModeCount = numRows+numRows-2
        oneModeColum = 1+numRows-2
        columNum = (strNum//oneModeCount)*oneModeColum+(strNum%oneModeCount//numRows)+(strNum%oneModeCount)%numRows
        a = []
        i = 0
        while i<numRows:
            tempLsit = []
            j = 0
            while j<columNum:
                   tempLsit.append("")
                   j = j+1
            a.append(tempLsit)
            i = i+1
        j = 0
        k = 0
        p = 0
        rowUp = True
        while j<len(s):
            a[k][p] = s[j]
            if k == 0:
                rowUp = True
            elif k == numRows - 1:
                rowUp = False
            if rowUp is True:
                k = k+1
            else:
                k = k-1
                p = p+1
            j = j+1            
        i = 0
        result = []
        while i<numRows:
            tempLsit = a[i]
            j = 0
            while j<columNum:
                   if tempLsit[j] != "":
                       result.append(tempLsit[j])
                   j = j+1
            i = i+1
        return "".join(result)

if __name__ == "__main__":
    s = Solution()
    print(s.convert("ab",1))