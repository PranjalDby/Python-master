# to Check the array is sorted or not

# Two- pointer approach
def isSorted(array,first_index,second_index)->bool:

    if len(array) <=1:
        return True
    
    if first_index != second_index and second_index <=len(array)-1:
        if array[first_index] > array[second_index]:
            return False
        
        return isSorted(array,first_index + 1,second_index + 1)
    
    return True

def sumElements(array,index=0,initialSum=0):
    # Base Case 1
    if len(array) <= 1:
        return 0 if len(array) == 0 else array[0]
    
    #Base Case 2
    if index >= len(array):
        return initialSum
    
    # Processing
    initialSum += array[index]
    
    #Recursive Relation
    return sumElements(array,index+1,initialSum)

def searchElement(array,size,element) -> bool:

    print(array)
    if size == 0:
        return False
    
    if array[0] == element:
        return True
    
    return searchElement(array[count+1:],size-1,element)


count = 0
def checkArray(array,index):
    if len(array) == 0:
        return
    
    print(array)
    checkArray(array[count+1:],index + 1)


# Binary search work on sorted array to do the searching amortized time complexity = Ω(logn) worst case complexity O(n)
    
def binarySearch(array,element,low,end)->bool:

    if low > end:
        return False

    mid = low + (end - low) // 2

    if array[mid] == element:
        return True

    if array[mid] < element:
        return binarySearch(array,element,mid+1,end) # right sub-array
    
    else:
        return binarySearch(array,element,low,mid-1) # left sub-array
    

array = [2,4,6,8,10,14,16]

# array = [1,-1]
# res = isSorted(array,0,1)
# print(sumElements(array))

# res = binarySearch(array,9,0,len(array)-1)

# String Operations Using recursion


