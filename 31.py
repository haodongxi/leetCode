from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        j = len(nums)-1
        swap = False
        while j>0:
            minIndex = (nums[1:j+1])[::-1].index(min(nums[1:j+1]))
            minIndex = len(nums[1:j+1]) - minIndex  
            if minIndex == j:
                j=j-1
            else:
                nums[minIndex],nums[j] = nums[j],nums[minIndex]
                swap = True
                break
        if swap == False:
            if nums.index(min(nums)) == 0:
                nums[0],nums[len(nums)-1] = nums[len(nums)-1],nums[0]
                # self.nextPermutation(nums)
            else :
                nums.reverse()
        print(nums)
if __name__ == "__main__":
    s = Solution()
    s.nextPermutation([2,3,1])
    # s.nextPermutation([2,1,3])
    # s.nextPermutation([1,3,2,4])
    s.nextPermutation([1,3,2])
    # s.nextPermutation([3,1])
    # s.nextPermutation([1,3])
    # s.nextPermutation([1])
