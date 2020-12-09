def isValid(s: str) -> bool:
    if len(s) == 0:
        return True
    if len(s)%2 != 0:
        return False
    if "()" in s or "{}" in s or "[]" in s:
        s = s.replace("()","")
        s = s.replace("{}","")
        s = s.replace("[]","")
        return isValid(s) 
    else :
        return False

def reverseSymbol(c):
    if c == "(":
        return ")"
    if c == "[":
        return "]"
    if c == "{":
        return "}"
    if c == ")":
        return "("
    if c == "]":
        return "["
    if c == "}":
        return "{"
    return ""
if __name__ == "__main__":
    print(isValid('([)]'))