from typing import List
def letterCombinations(digits: str) -> List[str]:
    mDict = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
    if len(str) == 0:
        return []
    if len(digits) == 1:
        return  [a for a in mDict[digits]]
    result  = []
    for a in mDict[digits[0]]:
        for x in letterCombinations(digits[1:]):
             result.append(a+x)
    return result

if __name__ == "__main__":
    print(letterCombinations('1'))