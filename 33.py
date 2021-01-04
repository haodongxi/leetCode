from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        return nums.index(target)
    def search2(self, nums: List[int], target: int) -> int:
        centerIndex = len(nums)//2
        i = 0
        j = len(nums)-1
        if nums[i]<nums[centerIndex]:
            #升序，旋转在后半段
            if target >= nums[i] and target<=nums[centerIndex]:
                #结果在此
                
                pass
            else:
                #结果后半段
                pass 
        if nums[i]>nums[centerIndex]:
            # 旋转在后半段
            if target >= nums[centerIndex+1] and target<=nums[j]:
                #结果在此
                pass
            else:
                #结果前半段
                pass 
        print(centerIndex)
def TwoDiv(nums,target):
    if len(nums)==1 :
        if target == nums[0]:
            print(1)
        else:
            print(-1)
        return
    if len(nums)==2 :
        if target == nums[0] or target == nums[1] :
            print(1)
        else:
            print(-1)
        return
    center = len(nums)//2
    if target<=nums[center]:
        TwoDiv(nums[0:center+1],target)
    else:
        TwoDiv(nums[center+1:],target)
if __name__ == "__main__":
    s = Solution()
    TwoDiv([4,5,6,7,8,9,0],6)
    # print(s.search2([3,4,5,6,7,8,1,2],7))
    # print(s.search2([5,6,7,8,0,1,2,3,4],3))
    # print(s.search2([5,6,7,0,1,2,3,4],5))
    # print(s.search2([5,10,11,12,9],5))
    # print(s.search2([10,11,0,2,3,4,],5))