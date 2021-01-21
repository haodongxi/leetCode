from typing import List
from functools import reduce

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        sum = reduce(lambda x,y: x+y,candidates)
        if sum<target:
            return []
        self.ssss = []
        candidates.sort()
        for index,a in enumerate(candidates):
            self.eachList(candidates[index:],target,[a])
        
        result = []
        for tempList in self.ssss:
            isAdd = True
            for a in tempList:
                aCount = tempList.count(a)
                cCount = candidates.count(a)
                if aCount>cCount:
                    isAdd = False
                    break
            if isAdd == True:
                result.append(tempList)

        return result

    def eachList(self,nums,target,ts):
        minNum = nums[0]
        if len(nums)==1:
             if minNum == target or target%minNum==0:
                y = target//minNum
                y = y-1
                for _ in range(0,y):
                    ts.append(minNum)
                if ts not in self.ssss:
                    self.ssss.append(ts)
                return True
             else:
                return  False
        if target<minNum:
            return False
        if minNum == target:
            if ts not in self.ssss:
                self.ssss.append(ts)
            return ts
        for i in range(0,len(nums)):
            ts1 = ts.copy()
            ts1.append(nums[i])
            self.eachList(nums[i:],target-nums[0],ts1)
if __name__ == "__main__":
    s = Solution()
    # print(s.combinationSum([10,1,2,7,6,1,5],8))
    # print(s.combinationSum([2,5,2,1,2],5))
    print(s.combinationSum([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],27))
