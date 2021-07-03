from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        i = 0
        jumpCount = 0
        while(i < len(nums)):
            tempNum = nums[i]
            if tempNum==0 or len(nums)==1:
                break
            if (tempNum+i)>=len(nums)-1:
                jumpCount = jumpCount+1
                break
            subNums = nums[i+1:i+tempNum+1]
            if len(subNums) == subNums.count(0):
                return 0
            if len(subNums)==0:
                break
            for j in range(0,len(subNums)):
                if subNums[j]!=0:
                    subNums[j] = subNums[j] + j
            maxNum = max(subNums)
            i = len(subNums) - subNums[::-1].index(maxNum)-1+i+1
            jumpCount = jumpCount + 1
        return jumpCount



if __name__ == '__main__':
    s = Solution()
    # print(s.jump([1,1,1,1]))
    print(s.jump([5,9,3,2,1,0,2,3,3,1,0,0]))