from typing import List
def maxArea(height: List[int]) -> int:
    if not height or len(height)==0:
        return 0
    length = len(height)
    dp = [[0 for d in range(length)] for c in range(length)]
    i = 0
    while i<length:
        j = i+1
        while j<length:
            dp[i][j] = max(min(height[i],height[j])*(j-i),dp[i][j-1])
            j = j+1
        i = i+1
    maxHeight = max([dp[c][length-1] for c in range(length)])
    return maxHeight
def maxArea2(height: List[int]) -> int:
    if not height or len(height)==0:
        return 0
    pass
if __name__ == "__main__":
    print(maxArea2([1,8,6,2,5,4,8,3,7]))