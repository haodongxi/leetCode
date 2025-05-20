

def find_p(arr ,low ,hight):
    i = low - 1
    pivot = arr[hight]
    for j in range(low,hight):
        if arr[j] <= pivot:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[hight],arr[i+1] = arr[i+1],arr[hight]
    return i + 1
def quick(arr ,low ,hight):
    if low >= hight:
        return
    p = find_p(arr,low,hight)
    quick(arr,low,p-1)
    quick(arr,p+1,hight)

def partition2(arr,low,high): 
    i = ( low-1 )         # 最小元素索引
    pivot = arr[high]     
  
    for j in range(low , high): 
  
        # 当前元素小于或等于 pivot 
        if   arr[j] <= pivot: 
          
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
  
 
# # arr[] --> 排序数组
# # low  --> 起始索引
# # high  --> 结束索引
  
# # 快速排序函数
def quickSort2(arr,low,high): 
    if low < high: 
        pi = partition(arr,low,high) 
        quickSort2(arr, low, pi-1) 
        quickSort2(arr, pi+1, high) 
  

def quick_sort_inplace(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1  # 初始化 high 为最后一个索引
    
    if low >= high:
        return  # 基线条件
    
    # 分区操作
    pivot_index = partition(arr, low, high)
    
    # 递归左右子数组
    quick_sort_inplace(arr, low, pivot_index - 1)
    quick_sort_inplace(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[high]  # 选择最后一个元素作为基准
    i = low - 1  # 指向小于基准的区域的最后一个位置
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # 交换位置
    
    # 将基准放到正确的位置
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1  # 返回基准的最终位置


def quick4(arr):
    if len(arr) <= 0:
        return []
    middle = arr[0]
    left = [i for i in arr if i<middle]
    middleArr = [i for i in arr if i==middle]
    right = [i for i in arr if i>middle]
    return quick4(left)+middleArr+quick4(right)
    

if __name__ == '__main__':
    arr = [2,3,6,1,3,5,5,3,]
    # quick(arr,0,len(arr)-1)
    # print(arr)
    res = quick4(arr)
    print(res)