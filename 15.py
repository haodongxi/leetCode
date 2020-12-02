from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    resultList = []
    for index, a in enumerate(nums):
        subList = nums[index+1:]
        target = 0 - a
        tempResultList = twoSum(subList, target)
        if len(tempResultList) > 0:
            for valueList in tempResultList:
                tempList = []
                tempList.append(a)
                for value in valueList:
                    tempList.append(nums[value+1+index])
                tempList.sort()
                if not tempList in resultList:
                    resultList.append(tempList)
    return resultList


def twoSum(nums: List[int], target: int):
    dict = {}
    result = []
    for index, a in enumerate(nums):
        dict[a] = index
    for index, a in enumerate(nums):
        j = dict.get(target - a)
        if j is not None and index != j:
            result.append([index, j])
    return result


def threeSum2(nums: List[int]) -> List[List[int]]:
    if len(nums) < 3:
        return []
    nums.sort()
    i = 0
    dict = {}
    while i < len(nums)-2:
        if nums[i] > 0:
            break
        if i>0 and nums[i]==nums[i-1]:
            i = i+1
            continue
        l = i+1
        r = len(nums)-1
        while l < r:
            if nums[i]+nums[l]+nums[r] == 0:
                # resultList.append([nums[i], nums[l], nums[r]])
                tempStr = "#".join([str(nums[i]),str(nums[l]),str(nums[r])])
                dict[tempStr]=1
                l = l+1
                r = r-1
            elif nums[i]+nums[l]+nums[r] > 0:
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
    print(threeSum2([0,0,0,0,0]))
