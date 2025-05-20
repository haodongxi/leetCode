


def sort1(arr):
    if len(arr)<=1:
        return arr
    middle = len(arr)//2
    left = sort1(arr[0:middle]) if middle > 0 else []
    right = sort1(arr[middle:]) if middle <= (len(arr)-1) else []
    return merge(left,right)
def merge(arr1,arr2):
    if arr1 == None and arr2 == None:
        return []
    if arr1 == None:
        return arr2
    if arr2 == None:
        return arr1

    i = 0
    j = 0
    arr = []
    while i<len(arr1) and j<len(arr2):
        if arr1[i] <= arr2[j]:
            arr.append(arr1[i])
            i+=1
            
        elif arr1[i] > arr2[j]:
            arr.append(arr2[j])
            j+=1
    arr+=arr1[i:]
    arr+=arr2[j:]
    return arr
arr = [2,3,6,1,3,5,5,3,]
res = sort1(arr)
print(res)


