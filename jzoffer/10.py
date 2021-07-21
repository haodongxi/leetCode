# -*- coding:utf-8 -*-
class Solution:
    a = {0:0,1:1,2:2}
    def rectCover(self, number):
        if number in list(self.a.keys()):
            return self.a[number]
        cu = 1
        if number-1 in list(self.a.keys()):
            cu = self.a[number-1]
        else:
            cu =  self.rectCover(number-1)
            self.a[number-1] = cu
        bu = 1
        if number-2 in list(self.a.keys()):
            bu = self.a[number-2]
        else:
            bu =  self.rectCover(number-2)    
            self.a[number-2] = bu
        return cu+bu
        

if __name__ == '__main__':
    s = Solution()
    print(s.rectCover(35))