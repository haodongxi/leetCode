from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        minZ = 1
        for index,a in enumerate(nums):
            if minZ in nums:
                minZ = minZ + 1
            else:
                return minZ
        return minZ



if __name__ == "__main__":
    s = Solution()
    s.firstMissingPositive([3,4,-1,1])
