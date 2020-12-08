from typing import List
def fourSum(nums: List[int], target: int) -> List[List[int]]:
    nums.sort()
    resultList = []
    for index in range(len(nums)-3):
        tempTarget = target - nums[index]
        threeSumList = threeSum2(nums[index+1:],tempTarget)
        for threeSum in threeSumList:
            threeSum.append(nums[index])
            threeSum.sort()
            if not threeSum in resultList:
                resultList.append(threeSum)
    return resultList



def threeSum2(nums: List[int],target) -> List[List[int]]:
    if len(nums) < 3:
        return []
    nums.sort()
    i = 0
    dict = {}
    while i < len(nums)-2:
        if i>0 and nums[i]==nums[i-1]:
            i = i+1
            continue
        l = i+1
        r = len(nums)-1
        while l < r:
            if nums[i]+nums[l]+nums[r] == target:
                tempStr = "#".join([str(nums[i]),str(nums[l]),str(nums[r])])
                dict[tempStr]=1
                l = l+1
                r = r-1
            elif nums[i]+nums[l]+nums[r] > target:
                r = r-1
            else:
                l = l+1
        i = i+1
    resultList = []
    for value in dict.keys():
        tempList = value.split("#")
        resultList.append([int(tempList[0]),int(tempList[1]),int(tempList[2])])
    return resultList
if __name__ == "__main__":
    print(fourSum([5,5,3,5,1,-5,1,-2],4))