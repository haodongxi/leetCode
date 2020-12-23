from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        delNum = 0
        for i in range(0,len(nums)):
            current =  nums[i-delNum]
            if current != val:
                n = n+1
            else:
                del nums[i-delNum]
                delNum = delNum+1
        return n
if __name__ == "__main__":
    s = Solution()
    a = [0,1,2,2,3,0,4,2]
    s.removeElement(a,2)
    print(a)