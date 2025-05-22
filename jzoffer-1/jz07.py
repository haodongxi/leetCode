from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums) < 3 :
            return []
        res = []
        for i in range(len(nums)):
            if i > len(nums)-3:
                break
            sub_res = self.twoSum(nums[i+1:],0-nums[i],nums[i])
            if len(sub_res) >0:
                res.extend(sub_res)

        lst = [tuple(row) for row in res]
        s = set(lst)
        lst = [list(row) for row in s]
        return lst
            


    def twoSum(self, numbers: List[int], target: int,addN) -> List:
        res = []
        for i in range(len(numbers)):
            num = numbers[i]
            diff = target - num
            if numbers[i+1:].count(diff) > 0:
                res.append(sorted([num,diff,addN]))
        return res


if __name__ == '__main__':
    s = Solution()
    res = s.threeSum([1,2,-2,-1])
    print(res)