from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
        for i in range(1,len(nums)):
            a = nums[i]
            b = target - a
            temp = nums[:i]
            if b in temp:
                return [i,temp.index(b)]
        return []
def twoSum1(nums, target):
    lens = len(nums)
    j=-1
    for i in range(1,lens):
        temp = nums[:i]
        if (target - nums[i]) in temp:
            j = temp.index(target - nums[i])
            break
    if j>=0:
        return [j,i]    
def twoSum2(nums, target):
        dict = {}
        for index,a in enumerate(nums):
                dict[a] = index
        for index,a in enumerate(nums):
             j = dict.get(target - a)
             if j is not None and index!=j:
                return [index,j]
if __name__ == "__main__":
    a = [2,3,3]
    print(twoSum2(a,6))
    