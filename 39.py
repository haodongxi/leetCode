from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ssss = []
        candidates.sort()
        for index,a in enumerate(candidates):
            self.eachList(candidates[index:],target,[a])
        return self.ssss

    def eachList(self,nums,target,ts):
        minNum = nums[0]
        if len(nums)==1:
             if minNum == target or target%minNum==0:
                y = target//minNum
                y = y-1
                for _ in range(0,y):
                    ts.append(minNum)
                self.ssss.append(ts)
                return True
             else:
                return  False
        if target<minNum:
            return False
        if minNum == target:
            self.ssss.append(ts)
            return ts
        for i in range(0,len(nums)):
            ts1 = ts.copy()
            # ts2 = ts.copy()
            ts1.append(nums[i])
            # ts2.append(nums[1])
            self.eachList(nums[i:],target-nums[0],ts1)
            # self.eachList(nums[1:],target-nums[0],ts2)
if __name__ == "__main__":
    s = Solution()
    # s.combinationSum([3,6,7],7)
    # s.combinationSum([2,3,6,7],14)
    # print(s.combinationSum([2,3,5],8))
    # s.combinationSum([2,3,4],8)
    # s.combinationSum([7],7)
    # s.combinationSum([6,7],7)
    # s.combinationSum([7,8],7)
    print(s.combinationSum([3,5,8],11))
