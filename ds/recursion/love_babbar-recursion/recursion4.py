def mergeSortCaller(arr,low,high)->int:
    temp = [0] * len(arr)

    return mergeSort(arr,low,high,temp=temp)

def mergeSort(a,low,high,temp)->int:
    if low >= high:
        return 0
    inversion = 0
    # print(low,high)
    mid = low + (high - low) // 2
    # for left-subarray
    # count inversioncount in left-part
    inversion += mergeSort(a,low,mid,temp)
    # for right-subarray
    # vice-versa
    inversion += mergeSort(a,mid + 1,high,temp)

    inversion += merge(arr,low,high,mid,temp)
    return inversion

def merge(arr,low,high,mid,temp)->int:
    i = low #index of left-part
    j = mid+1 #index of right-sub part
    k = low
    inversion_cnt_merge = 0
    while i<= mid and j <= high:
        if arr[i] < arr[j]:
            temp[k] = arr[i]
            k+=1
            i+=1
        else:
            temp[k] = arr[j]
            inversion_cnt_merge += (mid-i) + 1
            k+=1
            j+=1

    while i<=mid :
        temp[k] = arr[i]
        k+=1
        i+=1
    
    while j <= high:
        temp[k] = arr[j]
        k+=1
        j+=1
    
    # copied the element of sorted array into the original array
        
    for i in range(low,high+1):
        arr[i] = temp[i]

    return inversion_cnt_merge




arr = [1, 20, 6, 4, 5] 
inv = mergeSortCaller(arr,0,len(arr)-1)
print(arr)
print(inv)