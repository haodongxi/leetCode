def isPalindrome(x: int) -> bool:
    if x<0:
        return False
    s = str(x)
    if s == s[::-1]:
        return True
    else:
        return False
if __name__ == "__main__":
    print(isPalindrome(-1))