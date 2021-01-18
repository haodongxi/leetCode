from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        # for index,a in enumerate(candidates):
        #     print(a)
        # print(self.eachList(candidates[index:],target))
        print(self.eachList(candidates[0:],target))

    def eachList(self,nums,target):
        minNum = nums[0]
        if len(nums)==1:
            return True if minNum == target else False
        if target<minNum:
            return False
        if minNum == target:
            return True
        result = self.eachList(nums,target-nums[0])
        result1 = self.eachList(nums[1:],target-nums[0])

    
if __name__ == "__main__":
    s = Solution()
    # s.combinationSum([3,6,7],7)
    # s.combinationSum([2,3,6,7],7)
    s.combinationSum([2,3,5],8)
    # s.combinationSum([7],7)
    # s.combinationSum([6,7],7)
    # s.combinationSum([7,8],7)
