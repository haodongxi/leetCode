class Solution:
    def divide(self, a: int, b: int) -> int:
        max = 2**31 - 1
        min = -2**31


        fuhao = self.fuhao(a,b)
        t_a = abs(a)
        t_b = abs(b)
        fushu = False
        if fuhao  != True:
            fushu = True
        res = self.chufa(t_a,t_b)
        if fushu == True:
            res = 0 - res

        if res >= max:
            return max
        if res <= min:
            return min
        return res
    def fuhao(self,a,b):
        return abs(a)+abs(b) == abs(a+b)
    def chufa(self,a,b):
        res = 0
        while True:
            if a == 0:
                res = res + 0
                break
            if b > a:
                res = res + 0
                break
            res = res + 1
            a = a - b
        return res 
    def chengfa(self,a,b):
        if a == 0 or b == 0:
            return 0
        res = 0
        for i in range(b):
            res = res + a
        return res
    
    def chufaM(self,a,b):
        if(a < b):
            return str(0)
        aStr = str(a)
        if len(aStr) > 0:
            aFirst = int(aStr[0])
            if aFirst >= b:
                res = self.chufa(aFirst,b)
                if len(aStr[1:]) > 0:
                    subStr = self.chufaM(int(aStr[1:]),b )
                    if subStr != '-1':
                        return str(res) + subStr
                    else:
                        return str(res)
                else:
                    return str(res)  
            else:
                if len(aStr[1:]) > 0:
                    res = self.chufa(int(aStr[0:2]),b)
                    if len(aStr[2:]) > 0:
                        subStr = self.chufaM(int(aStr[2:]),b )
                        if subStr != '-1':
                            return  '0' + str(res) +  + subStr
                        else:
                           return '0' + str(res)
                    else:
                         return '0' + str(res)
        else:
            return str(-1)


if __name__ == '__main__':
    s = Solution()
    res = s.chufaM(100,2)

    # res = s.chengfa(-2,5)
    
    # res = s.divide(-2147483648,-1)
    print(int(res))
    