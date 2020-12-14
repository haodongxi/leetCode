from typing import List
def generateParenthesis(n: int) -> List[str]:
    if n == 0:
        return []
    if n == 1:
        return ["()"]
    dict = {}
    for item in generateParenthesis(n-1):
        for i in range(len(item)+1):
            j = i+1
            tempS = insertStr(item,"(",i)
            while j<=len(item)+1:
                tempS = insertStr(tempS,")",j)
                if isValid(tempS):
                    dict[str(tempS)] = 1
                j = j+1
    return list(dict.keys())
                
def insertStr(s,target,index):
    str_list = list(s)
    str_list.insert(index, target)
    a_b = ''.join(str_list)
    return a_b
def isValid(s: str) -> bool:
    if len(s) == 0:
        return True
    if len(s)%2 != 0:
        return False
    if "()" in s :
        s = s.replace("()","")
        return isValid(s) 
    else :
        return False 

if __name__ == "__main__":
    print(generateParenthesis(3))