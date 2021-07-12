# -*- coding:utf-8 -*-
class Solution:
    a = {}
    def Fibonacci(self, n):
        if n ==0:
            return 0
        if n in list(self.a.keys()):
            return self.a[n]
        if n == 1 or n == 2:
           self.a[n] = 1
           return 1
        cu = 1
        if n-1 in list(self.a.keys()):
            cu = self.a[n-1]
        else:
            cu =  self.Fibonacci(n-1)
            self.a[n-1] = cu
        bu = 1
        if n-2 in list(self.a.keys()):
            bu = self.a[n-2]
        else:
            bu =  self.Fibonacci(n-2)    
            self.a[n-2] = bu
        return cu+bu

if __name__ == '__main__':
    s = Solution()
    print(s.Fibonacci(39))