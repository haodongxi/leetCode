#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param array int整型一维数组 
# @return int整型一维数组
#
class Solution:
    def reOrderArray(self , array):
        for i in range(0,len(array)-1):
            j = 0
            while(j<len(array)-1-i):
                a = array[j]
                b = array[j+1]
                if self.isOS(a) and not self.isOS(b):
                     array[j],array[j+1] = array[j+1],array[j]
                j+=1
        return array  
    def reOrderArray2(self , array):
        nums = [0 for x in range(0,len(array))]
        i,head = 0,0
        j,tail = len(array)-1,len(array)-1
        while(i<len(array) and j>=0):
            if not self.isOS(array[i]):
                nums[head] = array[i]
                head +=1
            if self.isOS(array[j]):
                nums[tail] = array[j]
                tail-=1
            i += 1
            j -= 1
        return nums                      
    def isOS(self,n):
        if n%2 == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    print(s.reOrderArray2([1,2,3,4,5,6,7]))