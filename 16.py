from typing import List
def threeSumClosest( nums: List[int], target: int) -> int: 
    nums.sort()
    i = 0
    lastSum = None
    while i < len(nums)-2:
        l = i+1
        r = len(nums)-1
        subLastSum = None
        lastUp = None
        ch = None
        while l < r:
            nowSum = nums[i]+nums[l]+nums[r]
            nowCh = target - nowSum
            nowUp = None
            if  nowSum == target:
                return target
            elif (subLastSum == None and nowCh>0) or  (ch!=None and nowCh>ch):
                r = r-1
                nowUp = False
            else:
                l = l+1
                nowUp = True
            if lastUp==None or lastUp == nowUp:
                lastUp = nowUp
                subLastSum = nowSum
                ch = nowCh
            else:
                if nowSum>subLastSum:
                    break
                else :
                    subLastSum = nowSum
                    break
        if lastSum==None or (((target - subLastSum)< (target - lastSum)) if ((target - subLastSum)*(target - lastSum))<0 else (abs(target - subLastSum)< abs(target - lastSum))):
            lastSum = subLastSum
        i = i+1
    return lastSum

if __name__ == "__main__":
    print(threeSumClosest([1,1,1,0],-100))