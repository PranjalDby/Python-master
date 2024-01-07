def swap(s:str,i,j):
    n = len(s)
    s = list(s)
    if i <= n-1 and j <= n-1:
        temp = s[i];s[i] = s[j];s[j] = temp

    ss = ''
    for i in s:
        ss += i

    return ss

def reverseStr(s:str,low,end) -> str:
    if low > end:
        return s;

    s = swap(s,low,end)
    low += 1
    end -= 1
    return reverseStr(s,low,end)


def reverseStrModified(s:str)->str:
    if s == '':
        return ''
    
    return s[-1:] + reverseStrModified(s[:len(s)-1])


# Check palindrome

def checkPalindrome(original)->bool:
    if len(original) == 0 or len(original) == 1:
        return True
    
    if original[:1] == original[-1:]:
        #processing + recursive relation
        return checkPalindrome(original[1:len(original)-1])
    
    return False


# a ^ b

# a ^ b = b is even -> a ** b/2 x a ** b/2
# b is odd -> a * (a ** b/2 * a ** b/2)

def A2PowerB(a:int,b:int)->int:
    # base case
    if b == 0:
        return 1
    
    if b == 1:
        return a
    
    # RR
    ans = A2PowerB(a,b//2) # gives a ** b/2 

    if b % 2 == 0:
        return ans * ans
    
    else:
       return a * ans * ans


# t
def bubbleSort(array,n):
    if n == 1 or n == 0:
        return

    # Processing:
    #largest element ko end par pohchadega
    for i in range(n-1):
        if array[i] > array[i+1]:
            temp = array[i]
            array[i] = array[i+1]
            array[i+1] = temp
    
    bubbleSort(array,n-1)

def selectionSort(array,n,index):
    
    if index == n:
        return
    
    k = getMinimum(array,index,n-1)
    
    if k!=index:
        array[k],array[index] = array[index],array[k]


    selectionSort(array,n,index + 1)
    
def getMinimum(array,i,j)->int:
    if i==j:
        return i
    
    k = getMinimum(array,i+1,j)

    return i if array[i] < array[k] else k
        
# print(checkPalindrome('roottoor'))

# res1 = reverseStrModified('Pranjal1234')

array = [64, 25, 12, 22, 11]
# for i in range(len(array)):
#     smallest = i
#     for j in range(i+1,len(array)):
#         if array[smallest] > array[j]:
#             smallest = j

#     # Putting the element into the sorted array   
#     temp = array[i]
#     array[i] = array[smallest]
#     array[smallest] = temp

selectionSort(array,len(array),0)
print(array)