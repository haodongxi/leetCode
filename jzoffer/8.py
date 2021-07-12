# -*- coding:utf-8 -*-
class Solution:
    a = {}
    def jumpFloor(self, number):
        if number ==0:
            return 0
        if number in list(self.a.keys()):
            return self.a[number]
        if number == 1 :
           self.a[number] = 1
           return 1
        if number == 2 :
           self.a[number] = 2
           return 2   
        cu = 1
        if number-1 in list(self.a.keys()):
            cu = self.a[number-1]
        else:
            cu =  self.jumpFloor(number-1)
            self.a[number-1] = cu
        bu = 1
        if number-2 in list(self.a.keys()):
            bu = self.a[number-2]
        else:
            bu =  self.jumpFloor(number-2)    
            self.a[number-2] = bu
        return cu+bu

if __name__ == '__main__':
    s = Solution()
    print(s.jumpFloor(3))