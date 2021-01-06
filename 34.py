from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1,-1]
        startIndex = nums.index(target)
        endIndex = startIndex
        addNum = 1
        del nums[startIndex]
        while target in nums:
              endIndex  = addNum + nums.index(target)
              addNum = addNum + 1
              del nums[nums.index(target)]
        return [startIndex,endIndex]
if __name__ == "__main__":
    s = Solution()
    print(s.searchRange([],6))