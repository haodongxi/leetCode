from typing import List
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(words) == 0:
            return []
        result = []
        wordLength = len(words[0])
        for i in range(0,len(s)):
            tempStr = s[i:i+wordLength]
            if len(tempStr)!=wordLength:
                break
            if tempStr in words:
                destiTemp = [tempStr]
                j = i+wordLength
                while True:
                    if len(words) == len(destiTemp):
                        break
                    nextTempStr = s[j:j+wordLength]
                    if len(nextTempStr) == wordLength:
                         destiTemp.append(nextTempStr)
                    else:
                        break
                    j = j+wordLength
                if len(words) == len(destiTemp):
                    words.sort()
                    destiTemp.sort()
                    if words == destiTemp:
                        result.append(i)
        return result
if __name__ == "__main__":
    s = Solution()
    print(s.findSubstring("mississippi",['is']))