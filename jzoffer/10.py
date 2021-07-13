# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        if number == 0:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2
        return self.rectCover(number-1)*2-1
if __name__ == '__main__':
    s = Solution()
    print(s.rectCover(5))