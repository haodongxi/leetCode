# -*- coding:utf-8 -*-
class Solution:
    a = {}
    def jumpFloorII(self, number):
        if number ==0:
            return 1
        if number == 1 :
           self.a[number] = 1
           return 1
        if number == 2 :
           self.a[number] = 2
           return 2   
        sum = 0
        for i in range(0,number):
            u = 0
            if i in list(self.a.keys()):
                u = self.a[i]
            else:
                u = self.jumpFloorII(i)
                self.a[i] = u
            sum = sum + u
        return sum

if __name__ == '__main__':
    s = Solution()
    print(s.jumpFloorII(30))