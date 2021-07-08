# -*- coding:utf-8 -*-
from typing import no_type_check_decorator


class Solution:
    a = []
    b = []
    def push(self, node):
        # write code here
        self.a.append(node)
    def pop(self):
        if len(self.b)>0:
            return self.b.pop()
        else:
            while(len(self.a)>0):
                self.b.append(self.a.pop())
            return self.b.pop()
if __name__ == '__main__':
    s = Solution()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.pop())