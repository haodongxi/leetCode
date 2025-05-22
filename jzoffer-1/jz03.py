from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []

        for i in range(n+1):
            res.append(  int(str(bin(i)).count('1'))  )
    
        return res 

if __name__ == '__main__':
    s = Solution()
    res = s.countBits(5)
    print(res)