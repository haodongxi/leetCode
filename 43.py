from functools import reduce
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        sumList = []
        i = 0
        for a in num1[::-1]:
            inta = int(a)
            snum = 0
            tempSingleList = []
            for b in num2[::-1]:
                intb = int(b)
                tmuli = inta*intb+snum
                tsnum = tmuli//10
                tgnum = tmuli%10
                tempSingleList.append(tgnum)
                snum = tsnum
            if snum!=0:
                tempSingleList.append(snum)
            sumList.append(tempSingleList[::-1]+[ 0 for i in range(0,i)])
            i = i+1
        result = "".join(map(lambda x:str(x),reduce(lambda x,y:self.strSum(x,y),sumList))).lstrip('0')
        return result if len(result)>0 else '0'
        
    def strSum(self,num1,num2):
        num1 = num1[::-1]
        num2 = num2[::-1]
        numLength = max(len(num1),len(num2))
        y = 0
        numSum = []
        for index in range(0,numLength):
            a = num1[index] if index<len(num1) else 0
            b = num2[index] if index<len(num2) else 0
            tempSum = a+b+y
            y = tempSum//10
            s = tempSum%10
            numSum.append(s)
        if y !=0:
            numSum.append(y)
        return numSum[::-1]


if __name__ == "__main__":
    s = Solution()
    print(s.multiply('7','871'))
    # print(s.strSum([8,2],[2,3]))