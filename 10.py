class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s=" "+s
        p = " "+p
        if len(s)>20 or len(p)>30:
            return False
        
        dp = [[False for c in range(len(p)+2)] for r in range(len(s)+2)]
        dp[0][0] = True
        i = 1
        while i<=len(s):
            j = 1
            while j<=len(p):
                if s[i-1] == p[j-1] or p[j-1] == '.':
                        dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    if p[j-2] !=s[i-1] and p[j-2]!='.':
                        dp[i][j] = dp[i][j-2]
                    else:
                        dp[i][j]=dp[i][j-1] or dp[i][j-2] or dp[i-1][j];
                else:
                    dp[i][j]==False
                j = j+1
            i = i+1
        return dp[len(s)][len(p)]
if __name__ == "__main__":
    s = Solution()
    print(s.isMatch('aab','c*a*b'))