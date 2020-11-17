class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<1:
            return 0
        max = s[0]
        for i in range(0,len(s)):
            j = i+len(max)
            if j>len(s)-1:
                break
            else:
                tempStr = s[i:(j+1)]
                if self.haveFChar(tempStr):
                    continue
                else:
                    max = tempStr
                    if(j+1>len(s)-1):
                        break
                    tempMax:str = max
                    for k in range(j+1,len(s)):
                        tempMax = tempMax +s[k]
                        if self.haveFChar(tempMax):
                            break
                        else:
                            max = tempMax

            i = i+1
        return len(max)
    def haveFChar(self, s:str)->bool:
        dict = {}
        for i in range(0,len(s)):
            dict[s[i]] = i
        if len(dict) == len(s):
            return False
        else:
            return True
        
if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring('qaqevmf;lwf;le;lfl;ew'))