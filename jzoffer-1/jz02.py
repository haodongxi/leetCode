class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a2 = int(a,2)
        b2 = int(b,2)
        res = a2+b2
        result = str(bin(res))
        result = str.replace(result,'0b','')
        return result

if __name__ == '__main__':
    s = Solution()
    res = s.addBinary('11','10')
    print(res)