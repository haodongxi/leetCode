class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1_char_list = {}
        s2_char_list = {}

        if len(s1) > len(s2):
            return False
        for i in range(0,len(s1)):
            if s1[i] in s1_char_list.keys():
                s1_char_list[s1[i]] += 1
            else:
                s1_char_list[s1[i]] = 1
            if s2[i] in s2_char_list.keys():
                s2_char_list[s2[i]] += 1
            else:
                s2_char_list[s2[i]] = 1
        if s1_char_list == s2_char_list:
            return True
        if len(s1) == len(s2):
            return False
        
        for i in range(len(s1),len(s2)):

            pref = s2[i-len(s1)]
            s2_char_list[pref] -= 1

            if(s2_char_list[pref] == 0):
                del s2_char_list[pref]

            if s2[i] in s2_char_list.keys():
                s2_char_list[s2[i]] += 1
            else:
                s2_char_list[s2[i]] = 1
            if s1_char_list == s2_char_list:
                return True
        return False
if __name__ == '__main__':
    s = Solution()
    res = s.checkInclusion('ab','eidbaooo')
    print(res)

