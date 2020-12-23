class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        n = ""
        symbolZ = True
        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            symbolZ = True
        else:
            symbolZ = False
        dividend = abs(dividend)
        divisor = abs(divisor)
        if dividend < divisor:
            return 0
        strDividend = str(dividend)
        strDivisorLength = len(str(divisor))

        while True:
            tempStr = strDividend[0:strDivisorLength]
            tempDividend = int(tempStr)
            if len(tempStr) < strDivisorLength:
                n = n+'0'
                tempStr = strDividend[0:strDivisorLength+1]
                tempDividend = int(tempStr)
                if len(tempStr) < strDivisorLength:
                    break
                else:
                    s, y = JDD(tempDividend, divisor)
                    n=n+str(s)
                    strDividend = str(y) + strDividend[strDivisorLength+1:]
            else:
                s,y = JDD(tempDividend,divisor)
                n=n+str(s)
                strDividend = str(y) + strDividend[strDivisorLength:]
        print(str(n))
def JDD(dividend,divisor):
        n = 0
        while True:
            if dividend<divisor:
                break
            else:
                n = n+1
                dividend = dividend - divisor
        return (n,dividend)
if __name__ == "__main__":
    s = Solution()
    print(s.divide(300,3))
