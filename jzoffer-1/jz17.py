class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_l = len(s)
        t_l = len(t)
        if s_l < t_l:
            return ''
        if s == t:
            return s
        
        s_dict = {}
        t_dict = {}
        for i in t:
            t_dict[i] = (t_dict[i] if i in t_dict.keys() else 0 ) + 1

        for j in range(s_l):
            i = s[j]
            s_dict[i] = (s_dict[i] if i in s_dict.keys() else [] )
            s_dict[i].append(j)
        
        tem_s_dict = {}
        for k in t_dict.keys():
            v = t_dict[k]
            if k in s_dict.keys():
                s_word_list = s_dict[k]
                if len(s_word_list) >= v:
                    tem_s_dict[k] = s_word_list
                else:
                    return ''
            else:
                return ''
        
        temp_list = []
        for k in tem_s_dict.keys():
            temp_list.append(tem_s_dict[k])
        
        dkr_list = cartesian_product(temp_list)
        
        min_list = []
        for k_list in dkr_list:
            k_list.sort()
            if len(min_list) == 0:
                min_list = k_list
            else:
                diff_min =  min_list[len(min_list)-1] - min_list[0]
                diff_k =  k_list[len(k_list)-1] - k_list[0]
                if diff_k < diff_min:
                    min_list = k_list
        return s[ min_list[0]:min_list[len(min_list)-1]+1]


def cartesian_product(arrays):
    if not arrays:
        return [[]]
    result = []
    for x in arrays[0]:
        for y in cartesian_product(arrays[1:]):
            result.append([x] + y)
    return result

if __name__ == '__main__':
    s = Solution()
    res = s.minWindow("aa", "aa")
    print(res)