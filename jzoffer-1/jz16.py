class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        temp_str = ''
        pre = 0
        res = 0
        for i in range(len(s)):
            value = s[i]
            while pre < i and value in temp_str:
                temp_str = temp_str[1:]
                pre += 1
            temp_str = s[pre:i+1]
            res = max(res,len(temp_str))
        return res



if __name__ == '__main__':
    s = Solution()
    res = s.lengthOfLongestSubstring('bbbbb')
    print(res)