from typing import List
from functools import reduce

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        res = -1
        for k,v in enumerate(nums):
            left_sum =(0 if k == 0 else reduce(lambda x,y:x+y,nums[:k]))
            right_sum = 0 if k == len(nums)-1 else reduce(lambda x,y:x+y,nums[k+1:])
            if left_sum == right_sum:
                res = k
                break
        return res


    def pivotIndex2(self, nums: List[int]) -> int:
        res = -1
        sum = reduce(lambda x,y:x+y,nums)
        left_sum = 0
        right_sum = sum
        for k,v in enumerate(nums):
            right_sum = right_sum - v
            if right_sum == left_sum:
                res = k
                break
            else:
                left_sum += v
            

        return res


if __name__ == '__main__':
    s = Solution()
    res = s.pivotIndex2([1,7,3,6,5,6])
    print(res)