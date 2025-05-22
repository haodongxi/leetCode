from typing import List
from functools import reduce

class Solution:
    def numSubarrayProductLessThanK1(self, nums: List[int], k: int) -> int:
        
        res = []
        for i in range(0,len(nums)):
            self.quick(nums[i:],k,res)
        return len(res)


    def quick(self,nums: List[int],k,res):
        if len(nums) <= 0:
            return
        
        for i in range(0,len(nums)):
            sub_nums = nums[0:i+1]
            chengji = reduce(lambda a,b:a*b,sub_nums)
            if chengji < k:
                res.append(sub_nums)
            else:
                return

    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ans, prod, i = 0, 1, 0
        for j, num in enumerate(nums):
            prod *= num
            while i <= j and prod >= k:
                prod //= nums[i]
                i += 1
            ans += j - i + 1
        return ans



if __name__ == '__main__':
    s = Solution()
    res = s.numSubarrayProductLessThanK([1,1,1],2)
    print(res)