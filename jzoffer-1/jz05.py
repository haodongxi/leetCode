from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:


        max = 0
        for i in range(len(words)):
            str1 =  words[i]
            for j in range(len(words)):
                str2 = words[j]
                isSame = self.same(str1,str2)
                if isSame != True:
                   tempMax = len(str1) *len(str2)
                   if tempMax > max :
                       max = tempMax
        return max

    def same(self,str1,str2):
        # 将字符串转换为集合
        set1 = set(str1)
        set2 = set(str2)
        # 使用集合的交集操作找到两个字符串的交集
        intersection = set1.intersection(set2)
        return len(intersection) > 0

if __name__ == '__main__':
    s = Solution()
    res = s.maxProduct(["abcw","baz","foo","bar","fxyz","abcdef"])
    print(res)