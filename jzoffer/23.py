# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def VerifySquenceOfBST(self, sequence:List):
        if len(sequence)<3:
            return True
        if len(sequence)==3:

            if sorted(sequence) == sequence:
                return True
            if sorted(sequence,reverse=True) == sequence:
                return True
            if sequence[0]<sequence[1] and sequence[1]>sequence[2]:
                return True
            return False
        
        root = sequence[-1]
        sequence.pop()
        left = []
        right = []
        if len(sequence) == 3:
            return self.VerifySquenceOfBST(sequence)
        for a in sequence:
            if a<root:
                left.append(a)
            else:
                right.append(a)
        return self.VerifySquenceOfBST(left) and self.VerifySquenceOfBST(right)


if __name__ == '__main__':
    s = Solution()
    print(s.VerifySquenceOfBST([4,6,12,8,16,14,10]))