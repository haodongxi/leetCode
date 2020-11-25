from typing import List
def maxArea(height: List[int]) -> int:
    if not height or len(height)==0:
        return 0
    length = len(height)
    dp = [[0 for d in range(length)] for c in range(length)]
    i = 0
    maxHeight = 0
    while i<length:
        j = i+1
        while j<length:
            # dp[i][j] = max(min(height[i],height[j])*(j-i),dp[i][j-1])
            if min(height[i],height[j])*(j-i)>maxHeight:
                maxHeight = min(height[i],height[j])*(j-i)
            j = j+1
        i = i+1
    # maxHeight = max([dp[c][length-1] for c in range(length)])
    return maxHeight
def maxArea2(height: List[int]) -> int:
    if not height or len(height)==0:
        return 0
    length = len(height)
    i = 0
    j = length-1
    s = 0
    while i != j:
        if height[i]<height[j]:
            s = max(s,(j-i)*min(height[i],height[j]))
            i = i+1
        else:
            s = max(s,(j-i)*min(height[i],height[j]))
            j = j-1
    return s
def maxArea3(height: List[int]) -> int:
    if not height or len(height)==0:
        return 0
    length = len(height)
    i = 0
    j = length-1
    s = 0
    return dg(height,i,j,s)
def dg(height: List[int],i,j,s):
    if i == j:
        return s
    if height[i]>height[j]:
        j = j-1
    else :
        i = i+1
    s = max(s,(j-i)*min(height[i],height[j]))
    return dg(height,i,j,s)

if __name__ == "__main__":
    print(maxArea3([1,8,6,2,5,4,8,3,7]))