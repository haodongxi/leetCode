def myAtoi(s: str) -> int:
    s = s.strip(" ")
    isZ = True
    tempS = str(s)
    if tempS.startswith('-'):
        isZ = False
        s = s.replace("-","",1)
    if tempS.startswith("+"):
        s = s.replace("+","",1)
    resultStr = "0"
    for c in s:
        ac = ord(c)
        if ac>=48  and ac<=57:
            resultStr = resultStr+c
        else:
            break
    result = float(resultStr)
    if isZ is False:
        result = -result
    if result<-pow(2,31):
        return -int(pow(2,31))
    if result>(pow(2,31)-1):
        return int(pow(2,31)-1)
    return int(result)
if __name__ == "__main__":
    print(myAtoi("   +0 123"))