from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_l = len(s)
        p_l = len(p)
        if p_l > s_l:
            return []
        
        p_dict = {}
        s_dict = {}
        for i in p:
            p_dict[i] = (p_dict[i] if i in p_dict.keys() else 0)+1
        for i in s[0:p_l]:
            s_dict[i] = (s_dict[i] if i in s_dict.keys() else 0)+1
        res = []        
        if p_dict == s_dict:
            res.append(0)

        for i in range(p_l,s_l):
            
            s_dict[s[i-p_l]] = s_dict[s[i-p_l]] -1
            if s_dict[s[i-p_l]] == 0:
                del s_dict[s[i-p_l]]
            s_dict[s[i]] = (s_dict[s[i]] if s[i] in s_dict.keys() else 0)+1
            if p_dict == s_dict:
                res.append(i-p_l+1)
        return res

# class Solution:
#     def findAnagrams(self, s: str, p: str) -> List[int]:
#         s_len, p_len = len(s), len(p)
        
#         if s_len < p_len:
#             return []

#         ans = []
#         s_count = [0] * 26
#         p_count = [0] * 26
#         for i in range(p_len):
#             s_count[ord(s[i]) - 97] += 1
#             p_count[ord(p[i]) - 97] += 1

#         if s_count == p_count:
#             ans.append(0)

#         for i in range(s_len - p_len):
#             s_count[ord(s[i]) - 97] -= 1
#             s_count[ord(s[i + p_len]) - 97] += 1
            
#             if s_count == p_count:
#                 ans.append(i + 1)

#         return ans

if __name__ == '__main__':
    s = Solution()
    res = s.findAnagrams('cbaebabacd','abc')
    print(res)

