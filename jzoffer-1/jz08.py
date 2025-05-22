from typing import List


class Solution:
    def minSubArrayLen1(self, target: int, nums: List[int]) -> int:

        sum = {}
        for index in range(0,len(nums)):
            value = nums[index]
            for key in sum.keys():
                if sum[key][0] < target:
                    sum[key][0] = sum[key][0] + value
                    sum[key][1].append(index)
            sum[index] = [value,[index]]
        
        min = None
        res = None
        for key in sum.keys():
            value = sum[key][0]
            temp_res = len(sum[key][1])
            if value >= target and  (min == None or value <= min ) and ( res == None or temp_res < res):
                res = temp_res
                min = value
        return  0 if res == None else res
                
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        ans = n + 1
        start, end = 0, 0
        total = 0
        while end < n:
            total += nums[end]
            while total >= s:
                ans = min(ans, end - start + 1)
                total -= nums[start]
                start += 1
            end += 1
        
        return 0 if ans == n + 1 else ans                

    def min_self(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0
        tempSum = 0
        res = len(nums)+1
        left = 0
        for i in range(0,len(nums)):
            value = nums[i]
            tempSum += value
            while tempSum >= target:
                res = min(i - left+1,res)
                tempSum -= nums[left]
                left += 1
        return 0 if res == len(nums) + 1 else res  


if __name__ ==  '__main__':
    s = Solution()
    res = s.min_self(7,[2,3,1,2,4,3])
    print(res)