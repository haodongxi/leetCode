from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(numbers)):
            dict[numbers[i]] = i
        
        for i in range(len(numbers)):
            num = numbers[i]
            diff = target - num
            if dict.get(diff) != None:
                return [i,dict[diff]]
        return []


if __name__ == '__main__':
    s = Solution()
    res = s.twoSum([1,2,4,6,10],8)
    print(res)