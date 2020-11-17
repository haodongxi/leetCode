class Solution:
    def longestPalindrome(self, s) -> str:
        if len(s) == 0:
            return ""
        i = 0
        maxStr = s[0]
        while i < len(s):
            j = len(s)
            while j > i:
                subStr = s[i:j]
                reSubStr = subStr[::-1]
                if subStr == reSubStr and len(reSubStr) > len(maxStr):
                    maxStr = subStr
                    break
                j = j-1
            i = i+1
        return maxStr

    def longestPalindrome1(self, s) -> str:
        if len(s) == 0:
            return ""
        i = 0
        maxStr = s[0]
        while i < len(s):
            j = 1
            while True:
                q = i-j
                r = i+j
                if q >= 0 and r < len(s):
                    tempStr = s[q:r+1]
                    if s[q] == s[r]:
                        if len(maxStr) < len(s[q:r+1]):
                            maxStr = tempStr
                    else:
                        break
                else:
                    break
                j = j+1
            a = i-0.5
            k = 1
            while True:
                q = int(a-k+0.5)
                r = int(a+k-0.5)
                if q >= 0 and r < len(s):
                    tempStr = s[q:r+1]
                    if s[q] == s[r]:
                        if len(maxStr) < len(s[q:r+1]):
                            maxStr = tempStr
                    else:
                        break
                else:
                    break
                k = k+1
            i = i+1
        return maxStr
if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome1("bbabbbbbbbbb"))
