from typing import List
def longestCommonPrefix(strs: List[str]) -> str:
    if len(strs)==1:
        return strs[0]
    if len(strs)==0:
        return ""
    maxPre = ""
    i = 0
    minStr = strs[0]
    for string in strs:
        if len(string)<len(minStr):
            minStr = string
    strs.remove(minStr)
    while i<len(minStr):
        tempStr = minStr[0:i+1]
        is_common = True
        for string in strs:
            if not string.startswith(tempStr):
                is_common = False
                break
        if is_common == True:
            maxPre = tempStr
            i = i+1
        else:
            break
    return maxPre
            
    
if __name__ == "__main__":
    print(longestCommonPrefix(["ab","a"]))