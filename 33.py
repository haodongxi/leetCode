from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        return nums.index(target)

    def search3(self, nums: List[int], target: int) -> int:
        num = self.search2(nums,target)
        return -1 if num<0 else num

    def search2(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if target == nums[0]:
                return 0
            return -10000
        if len(nums) == 2:
            if target == nums[0]:
                return 0
            elif target == nums[1]:
                return 1
            return -10000
        if len(nums)==0:
            return -10000
        centerIndex = len(nums)//2
        if nums[0] < nums[centerIndex]:
            # 升序，旋转在后半段
            if target >= nums[0] and target <= nums[centerIndex]:
                # 在此
                #print('1-前半段')
                return TwoDiv(nums[0:centerIndex+1],target)
            else:
                #print('1-后半段')
                return centerIndex+self.search2(nums[centerIndex:],target)
        elif nums[len(nums)-1] > nums[centerIndex]:
            # 升序 旋转在前半段
            if target >= nums[centerIndex] and target <= nums[len(nums)-1]:
                # 在此
                return centerIndex+TwoDiv(nums[centerIndex:],target)
            else:
                #print('2-前半段')
                return self.search2(nums[0:centerIndex+1],target)
        else:
            print('出现bug')
        ## print(centerIndex)


def TwoDiv(nums, target):
    if len(nums) == 1:
        if target == nums[0]:
            return 0
        return -10000
    if len(nums) == 2:
        if target == nums[0]:
            return 0
        elif target == nums[1]:
            return 1
        return -10000
    center = len(nums)//2
    if target <= nums[center]:
        return TwoDiv(nums[0:center+1], target)
    else:
        return center +1+ TwoDiv(nums[center+1:], target)

if __name__ == "__main__":
    s = Solution()
    ## print(TwoDiv([5],5))
    ## print(TwoDiv([4,5,6,7,8,9],5))
    print(s.search3([3, 4, 5, 6, 7, 8, 1, ], 0))
    print(s.search3([5, 6, 7, 8, 0, 1, 2, 3, 4], 3))
    print(s.search3([5, 6, 7, 0, 1, 2, 3, 4], 5))
    print(s.search3([5, 10, 11, 12, 9], 5))
    print(s.search3([10, 11, 0, 2, 3, 4], 10000))
    print(s.search3([10], 2))
    print(s.search3([1,3], 0))
    print(s.search3([3,1], 3))
    print(s.search3([5,1,3],1))
    
