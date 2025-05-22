

def bubble(arr):
    for i in range(0,len(arr)-1):
        for j in range(0,len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j] 
        
    return arr

def dg_bubble(arr):
    if len(arr)<=1:
        return arr
    for i in range(0,len(arr)-1):
        if arr[i] > arr[i+1]:
            arr[i],arr[i+1] = arr[i+1],arr[i]
    return dg_bubble(arr[0:len(arr)-1])+[arr[-1]]

arr = [2,3,6,1,3,5,5,3,]
res = dg_bubble(arr)
print(res)
