class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        lastResult = self.countAndSay(n-1)
        tempArr = []
        for a in lastResult:
            if len(tempArr) == 0:
                numArr = []
                numArr.append(a)
                tempArr.append(numArr)
            else:
                lastNumArr = tempArr[-1]
                lastNum = lastNumArr[0]
                if a == lastNum:
                    lastNumArr.append(a)
                else:
                    numArr = []
                    numArr.append(a)
                    tempArr.append(numArr)
        result = ""
        for l in tempArr:
            result = result+str(len(l))+l[0]
        return result
            


if __name__ == "__main__":
    s = Solution()
    print(s.countAndSay(5))