# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        if len(pushV) == 0:
            return False
        if pushV == None:
            return False
        push_help_list = []
        while True:
            if len(push_help_list) == 0:
                if len(pushV)>0:
                    push_help_list.append(pushV[0])
                    pushV.remove(pushV[0])
                else:
                    break
            if push_help_list[-1] == popV[0]:
                push_help_list.pop()
                popV.remove(popV[0])
            else:
                if len(pushV)>0:
                    push_help_list.append(pushV[0])
                    pushV.remove(pushV[0])
                else:
                    break
        if len(pushV) == 0 and len(popV) == 0:
            return True
        else:
            return False
if __name__ == '__main__':
    s = Solution()
    print(s.IsPopOrder([1,2,3,4,5],[4,5,3,2,1]))