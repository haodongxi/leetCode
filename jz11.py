
from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        maxLength = 0
        map = {0:-1}
        counter = 0
        n = len(nums)
        for i in range(0,n):
            num = nums[i];
            if (num == 1):
                counter += 1 
            else:
                counter -= 1
            
            if (counter in  map.keys()) :
                prevIndex = map.get(counter)
                maxLength = max(maxLength, i - prevIndex)
            else:
                map[counter] =  i
        return maxLength


if __name__ == '__main__':
    s = Solution()
    res = s.findMaxLength([1,1,0,0,0,1])
    print(res)