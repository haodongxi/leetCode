from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lastNum = None
        n = 0
        delNum = 0
        for i in range(0,len(nums)):
            if lastNum == None:
                lastNum = nums[i-delNum]
                n = n+1
            elif lastNum == nums[i-delNum]:
                del nums[i-delNum]
                delNum = delNum+1
            else:
                lastNum = nums[i-delNum]
                n = n+1
        return n
                
if __name__ == "__main__":
    s = Solution()
    print(s.removeDuplicates([1]))