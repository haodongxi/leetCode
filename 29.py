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
            if tempDividend < divisor:
                tempStr = strDividend[0:strDivisorLength+1]
                tempDividend = int(tempStr)
                if len(tempStr) <= strDivisorLength:
                    n = n+'0'
                    break
                else:
                    if tempDividend < divisor:
                        n = n+'0'
                        strDividend = strDividend[strDivisorLength:]
                    else :
                        s, y = JDD(tempDividend, divisor)
                        n=n+str(s)
                        if len(strDividend[strDivisorLength+1:])==0:
                            break
                        else:
                            strDividend = (str(y) if y!=0 else "") + strDividend[strDivisorLength+1:]
            else:
                s,y = JDD(tempDividend,divisor)
                n=n+str(s)
                # strDividend = str(y) + strDividend[strDivisorLength:]
                if len(strDividend[strDivisorLength:])==0:
                    break
                else:
                    strDividend = str(y)+strDividend[strDivisorLength:]
        tempN = abs(float(n)) if symbolZ == True else -abs(float(n))
        if tempN<-pow(2,31):
            return -pow(2,31)
        if tempN>(pow(2,31)-1):
            return pow(2,31)-1
        return int(n) if symbolZ==True else -int(n)
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
    print(s.divide(-1060849722,99958928))
    print(s.divide(99,2))
    print(s.divide(7,-3))
    print(s.divide(100,2))
    print(s.divide(2147483647,2))
    
