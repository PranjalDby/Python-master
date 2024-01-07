def insertionSort(array,n,index):
    if index == n:
        return
    
    for i in range(n):
        if array[index] < array[i]:
            temp = array[i]
            array[i] = array[index]
            array[index] = temp

    insertionSort(array,n,index + 1)

# first approach
def merge(arr,s,e,mid):
    n  = e - s + 1
    res = []
    for i in range(e-s + 1):
        res.append(i)
    x = s
    y = mid + 1 
    z = 0
    while x <= mid and y <= e:
        if arr[x] < arr[y]:
            res[z] = arr[x]
            z+=1
            x+=1
        else:
            res[z] = arr[y]
            z+=1
            y+=1

    while x<= mid:
        res[z] = arr[x]
        z+=1
        x+=1
    
    while y<= e:
        res[z] = arr[y]
        z+=1
        y+=1

    for i in range(s,e + 1):
        arr[i] = res[i-s]
    

def mergeSort(arr,s,e):
    if s < e:
        mid = s + (e-s) // 2 # to ensure that sum will never cross the limit of integer
        mergeSort(arr,s,mid)
        mergeSort(arr,mid+1,e)
        merge(arr,s,e,mid)
    
array = [5,2,6,1,11,9,10]

# insertionSort(arr,len(arr),1)
mergeSort(array,0,len(array)-1)
print(array)
