from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        currentnum =nums[0]
        subResultNums = self.permuteUnique(nums[1:])
        result = []
        for subNums in subResultNums:
            length = len(subNums)
            for i in range(0,length+1):
                tempSubNums = subNums.copy()
                tempSubNums.insert(i,currentnum)
                if tempSubNums not in result:
                    result.append(tempSubNums)
        return result
if __name__ == '__main__':
    s = Solution()
    print(s.permuteUnique([1,1,2]))