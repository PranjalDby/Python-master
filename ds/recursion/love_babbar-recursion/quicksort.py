def quickSort(arr,low,high):
    if low >= high:
        return
    
    p = partition(arr,low,high)
    quickSort(arr,low,p-1) # for element less than pivot or  p
    quickSort(arr,p+1,high)# right part from the pivot


def partition(arr,low,high):
    pivot = arr[low]
    
    # counting elements less than pivot
    count = 0
    for i in range(low+1 ,high+1):
        if arr[i] <= pivot:
            count += 1
    
    # putting the pivot to its right place
    pivot_index = low + count
    temp = arr[pivot_index]
    arr[pivot_index] = pivot
    arr[low] = temp

    # left and right part from pivot
    i = low
    j = high
    while (i< pivot_index and j > pivot_index):
        
        # if they are at their correct position
        while arr[i] <= pivot:
            i+=1

        while arr[j] > pivot:
            j-=1

        # else i >pivot and j < pivot
        if i< pivot_index and j > pivot_index:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i+=1
            j-=1

    
    return pivot_index
        

arr = [10,5,7,1,8,9] 

quickSort(arr,0,len(arr)-1) 
print(arr)


    
