from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            for index,a in enumerate(nums):
                if a>=target:
                    return index
            return len(nums)
if __name__ == "__main__":
    s = Solution()
    print(s.searchInsert([1,3,5,6],3))