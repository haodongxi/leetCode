# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        if len(array)==0:
            return False
        if len(array[0])==0:
            return False
        if len(array[0]) == 1:
            if array[0][0] == target:
                return True
            else :
                return False
        top_right = array[0][len(array[0])-1]
        if target == top_right:
            return True
        if target>top_right:
            tempArr = []
            for (index,a) in enumerate(array):
                if index != 0:
                    tempArr.append(a)
            if len(tempArr) == 0:
                return False
            else:
                return self.Find(target,tempArr)
        if target<top_right:
            tempArr = []
            for (index,a) in enumerate(array):
                    tempArr.append(a[0:len(a)-1])
            return self.Find(target,tempArr)
if __name__ == '__main__':
    s = Solution()
    print(s.Find(7,[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]))