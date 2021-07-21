# -*- coding:utf-8 -*-
class Solution:
    a = {0:1}
    def Power(self, base, exponent):
        if base == 0:
            return 0
        if exponent == 1:
            return base
        result = self.Power2(base,abs(exponent))
        if exponent <0:
            result = 1/result
        return result

    def Power2(self, base, exponent):
            if base == 0:
                return 0
            if exponent == 1:
                return base
            if exponent in list(self.a.keys()):
                return self.a[exponent]
            result = base*self.Power2(base,exponent-1)
            self.a[exponent] = result
            return result
if __name__ == '__main__':
    s = Solution()
    print(s.Power(2.000,-1))