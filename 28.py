class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        for i in range(0,len(haystack)-len(needle)+1):
            tempStr = haystack[i:i+len(needle)]
            if tempStr == needle:
                return i
        return -1

if __name__ == "__main__":
    s = Solution()
    print(s.strStr('aaaaa','bba'))
    