


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if s == None or  len(s) == 0:
            return 0
        left = 0
        max_length = 1
        num_set = set()
        for i in range(len(s)):
            if left > i or i >= len(s):
                break
            if s[i] in num_set:
                for j in range(left,i):
                    if s[j] == s[i]:
                        left += 1
                        num_set.remove(s[j])
                        break
                    else:
                        left += 1
                        num_set.remove(s[j])

            num_set.add(s[i])
            i += 1
            max_length = len(num_set) if len(num_set)>max_length else max_length

        return max_length



if __name__ == '__main__':
    s = Solution()
    res = s.lengthOfLongestSubstring('abccaabg')
    print(res)