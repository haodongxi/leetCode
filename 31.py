from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums)-1
        minIndex = -1
        needSwapindex = -1
        swap = False
        while i>1:
            j = i
            while j>0:
                if nums[j] >= nums[i]:
                    j=j-1
                else:
                    if j>minIndex:
                        minIndex = j
                        needSwapindex = i
                    swap = True
                    break
            i = i-1
        if swap == True:
            nums[minIndex],nums[needSwapindex] = nums[needSwapindex],nums[minIndex]
        if swap == False:
            des = GetMinDistanceNum(nums,nums[0])
            if des!=None:
                tempIndex = nums.index(des)
                nums[0],nums[tempIndex] = nums[tempIndex],nums[0]
                temp = nums[1:]
                temp.sort()
                for index, a in enumerate(temp):
                    nums[index+1] = a
            else:
                nums.reverse()
        else :
            temp = nums[minIndex+1:]
            temp.sort()
            for index, a in enumerate(temp):
                nums[index+minIndex+1] = a
        print(nums)

def GetMinDistanceNum(nums,num):
    distance = None
    destination = None
    for a in nums:
        tempDis = a - num
        if tempDis>0 and(distance == None or tempDis<distance):
            distance = tempDis
            destination = a
    return destination



if __name__ == "__main__":
    s = Solution()
    s.nextPermutation([4,2,0,2,3,2,0])
    s.nextPermutation([1,2,0,3,0,1,2,4])
    s.nextPermutation([5,4,7,5,3,2])
    s.nextPermutation([1,4,3,1])
    s.nextPermutation([1,2,3,1])
    s.nextPermutation([2,3,1])
    s.nextPermutation([2,1,3])
    s.nextPermutation([1,3,2,4])
    s.nextPermutation([1,3,2])
    s.nextPermutation([3,1])
    s.nextPermutation([1,3])
    s.nextPermutation([1])
    s.nextPermutation([5,4,3,2,1])
