# -*- coding:utf-8 -*-


class Solution:
    def NumberOf1(self, n):
        a = []
        zn = n
        for i in range(0,32):
            a.append(pow(2,i))
        i = 0
        sum = 0
        while(True):
            if zn == 0:
                break
            if zn == a[i]:
               sum = sum +1
               break
            if zn < a[i] or (zn>a[i] and i == (len(a)-1)):
                if zn<a[i]:
                    zn = zn - a[i-1]
                else:
                    zn = zn - a[i]
                i = 0
                sum = sum+1
                continue
            i = i+1
        return sum

            
if __name__ == '__main__':
    s = Solution()
    print(s.NumberOf1(11))