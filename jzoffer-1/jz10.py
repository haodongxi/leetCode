from typing import List
from functools import reduce

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res,i,add = 0,0,0

        for j in range(0,len(nums)):
            value = nums[j]
            add += value
            while i<=j and add > k:
                add -= nums[i]
                i = i+1
            if add == k and i<=j:
                res += 1
        return res



if __name__ == '__main__':
    s = Solution()
    res = s.subarraySum([-1,-1,1],0)
    print(res)