class Solution:
    def longestValidParentheses(self, s: str) -> int:
        result = 0
        tempS = s
        lastIndex = -1
        while True:
            if "()" in s:
                index = tempS.index("()")
                if lastIndex == -1 or (lastIndex)
                # tempS = tempS.replace("()","")


if __name__ == "__main__":
    s = Solution()
    s.longestValidParentheses('()()')