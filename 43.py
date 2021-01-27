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
                tsnum = (inta*intb)//10
                tgnum = (inta*intb)%10
                tempSingleList.append(tgnum+snum)
                snum = tsnum
            if snum!=0:
                tempSingleList.append(snum)
            sumList.append(tempSingleList[::-1]+[ 0 for i in range(0,i)])
            i = i+1
        print(sumList)



if __name__ == "__main__":
    s = Solution()
    s.multiply('120','130')