from typing import List
def threeSumClosest( nums: List[int], target: int) -> int: 
    nums.sort()
    i = 0
    maxSum = None
    while i < len(nums)-2:
        l = i+1
        r = len(nums)-1
        subMaxSum = None
        while l < r:
            nowSum = nums[i]+nums[l]+nums[r]
            if  nowSum == target:
                return target
            p = l+1
            q = r-1
            pSum = nowSum
            qSum = nowSum
            if p<r:
                pSum = nums[i]+nums[p]+nums[r]
            if q>l:
                qSum = nums[i]+nums[l]+nums[q]
            pChar = abs(pSum - target)
            qChar = abs(qSum - target)
            if pChar<qChar:
                l = p
            else:
                r = q
            if subMaxSum == None or abs(target-subMaxSum)>abs(target-nowSum):
                subMaxSum = nowSum
        if maxSum == None or abs(target-maxSum)>abs(target-subMaxSum):
            maxSum = subMaxSum
        i = i+1
    return maxSum

if __name__ == "__main__":
    print(threeSumClosest([0,0,0,1],1))