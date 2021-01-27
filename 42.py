from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        for index,a in enumerate(height):
            left = height[:index]
            right = height[index+1:]
            if len(left)==0 or len(right)==0:
                continue
            leftMax = max(left)
            rightMax = max(right)
            short = min(leftMax,rightMax)
            if short>a:
                result = result + short - a
        return result


if __name__ == "__main__":
    s = Solution()
    # print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
    print(s.trap([]))
