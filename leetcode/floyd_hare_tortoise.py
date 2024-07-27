# this algorithms applies when question guarantees that only single number should be repeated more than once and items inside the array is less than size of array

nums = [3,1,3,4,2];


nums2 = sorted(nums)
print(nums2)
duplicate = -1
i = 0;j = 0
while(i<len(nums2)-1):
    if nums2[i] == nums2[i+1]:
        duplicate = nums2[i]
        break
    
    i+=1

print(duplicate)



# applying floyd's hare and tortoise O(1) space and linear time

def hare_tortoise(nums):

    hare = nums[0]
    tortoise = nums[0]

    while(True):
        tortoise = nums[tortoise]
        hare  = nums[nums[hare]]
        if tortoise == hare:
            break;

    hare = nums[0]
    while tortoise != hare:
        tortoise = nums[tortoise]
        hare = nums[hare]

    return hare




nums1 = [4,2,1,3,1]
print("Hare AND TORTOISE",hare_tortoise(nums1))
# Two Sum

nums = [3,2,3]
target = 6
def solve(nums,target):
    # for i in range(len(nums)):
    #     for j in range(i+1,len(nums)):
    #         if nums[i] + nums[j] == target:
    #             return [i,j]

    for k in range(len(nums)):
        sub = target-nums[k]
        if(nums.count(sub) > 0 and nums.index(sub) != k):
            return [nums.index(sub),k][::-1]

    return []


# ss = solve(nums,target)
# print(ss)

# palindromic string

s = ""
import math
import sys
from typing import List
sys.setrecursionlimit(100000)
def validPalindrom(s):
    if s == "":
        return True
    
    if s[0] == s[-1]:
        s = s[1:-1]
        return validPalindrom(s)
    
    return False


# def find_sum_of_three(nums, target):

#     nums = sorted(nums) # sort the array in ascending order
#     for curr in range(0,len(nums)):
#         for low in range(i+1,len(nums)):
#             for high in range(low+1,len(nums)):
#                 # check if sum is equal to target or not
#                 if (nums[curr] + nums[low] + nums[high]) == target:
#                     return True
                
    
#     return False

def solve3(nums,high,target,count):
    if count == 3 and target == 0:
        return True
    
    if count == 3 or high == 0 or target < 0:
        return False
    
    return solve3(nums,high-1,target-nums[high-1],count+1) or solve3(nums,high-1,target,count)
    

# Top k elements

class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None


def create_bst(root,data):
    if root == None:
        r = Node(data)
        root = r
        return root
    
    if root.data < data:
        root.left = create_bst(root.left,data)
    
    else:
        root.right = create_bst(root.right,data)

    
    return root

def print_bst(root):
    if root == None:
        return
    
    print_bst(root.left)
    print(root.data)
    print_bst(root.right)


def topKFrequent(nums: List[int], k: int) -> List[int]:
    hash_map = [[] for i in range(len(nums)+1)]
    count = {}
   
    for i in nums:
        count[i] = 1 + count.get(i,0)

    print(count)
    for (key,v) in count.items():
        hash_map[v].append(key)
    
    print(hash_map)
    
    i = len(nums)-1
    res = []
    for i in range(len(hash_map)-1,-1,-1):
        for n in hash_map[i]:
            res.append(n)
            if len(res) == k:
                return res





def bst(arr,k):
    root = None
    for i in range(len(arr)):
        root = create_bst(root,arr[i]);

    print_bst(root)


def solve4(arr,i,j,k):
    if k == j or j == len(arr) or i == len(arr):
        return []
    
    sum = arr[i] + arr[j] + arr[k]
    ans = []
    if sum == 0:
        ans.append([(arr[i],arr[j],arr[k]),solve4(arr,i+1,j+1,k-1)])

    ans.append([solve4(arr,i+1,j,k-1),solve4(arr,i+1,j+1,k)])

    return ans

n = [1,2,2,3,3,3]


# Valid Paranthesis
def isValid(s: str,stack:List[str]) -> bool:
    # firstly we iterate through the string and put the opening brackets into the stack

    for i in s:
        if i in ['(','[','{']:
            stack.append(i)
        else:
            # if it is not a opening bracket
            if (i == ')' and stack[-1] != "(") or (i == '}' and stack[-1] != "{") or (i == ']' and stack[-1] != "["):
                return False
            
            stack.pop()

    return True


s = "([{)])"
print(isValid(s,[]))


#  Find the Index of the First Occurrence in a String

def solve(hay,needle):
    i = 0
    while i < len(hay):
        if(hay[i:len(needle)+i] == needle):
            return i
        
        i+=1
       
    return -1

# return length of last-word

def solve2(s:str):
    s = s.strip()
    splitted = s.split(' ')
    
    return len(splitted[-1])

haystack = " robin walt moon ";needle = "walt"
print(solve2(haystack))

# Plus One
def solve3(digit:List[int]):
    n = len(digit)-1
    res = 0
    for i in range(0,len(digit)):
        res = res + (digit[i] * (10 ** n))
        n-=1

    r = []
    
    res +=1
    while(res != 0):
        remainder = res % 10
        r.append(remainder)
        res = res//10

    print(r[::-1])

digit = [1,2,3]
solve3(digit)

# binary add

a = '11'
b = '1'

def solve4(a,b):
    len_a = 0
    len_b = 0
    a1 = int(a)
    b1 = int(b)

    dec_eq_a = 0
    dec_eq_b = 0

    while(a1 != 0):
        res = a1 & 1
        dec_eq_a += (2 ** len_a) * res
        len_a +=1
        a1 = a1//10

    while(b1 != 0):
        res = b1 & 1
        dec_eq_b += (2 ** len_b) * res
        len_b +=1
        b1 = b1//10


    print(dec_eq_a,dec_eq_b)


    add = dec_eq_a + dec_eq_b
    re = []
    while(add != 0):
        re.append(add & 1)
        add = add >> 1
    
    re = re[::-1]
    re = list(map(lambda s:str(s),re))
    s = "".join(re)

    print(s)
    
def solve5(x):
    if x == 0:
        return 0
    
    if x == 1:
        return 1
    

    start = 0
    end = x

    while(start <= end):
        mid = start + (end - start) // 2

        if mid ** 2 > x:
            end = mid-1
        
        elif mid ** 2 < x:
            start = mid+1
        
        else:
            return mid
        
        
        # if it is odd number we have to return the value less actual root
        return end


def solve6(n):

    if n < 0:
        return 0
    
    if n == 0:
        return 1
    
    ans_1 = 0
    ans_2 = 0
    # taking 1 step
    ans_1 = ans_1 + solve6(n-1)

    ans_2 = ans_2 + solve6(n-2)

    return ans_1 + ans_2

def solve6_memo(n,dp):
    if n < 0:
        return 0
    
    if n == 0:
        return 1
    
    if dp[n] != -1:
        return dp[n]
    ans_1 = 0
    ans_2 = 0
    # taking 1 step
    ans_1 = ans_1 + solve6(n-1)

    ans_2 = ans_2 + solve6(n-2)

    dp[n] = ans_1 + ans_2

    return dp[n]

def solve6_tab(n):
    # dp = [0] * (n+1)

    # dp[0] = 1 # according our condition
    # # in recurence we traverse n-1...0 but this is tabulation or bottom -up we do just opposite
    # for i in range(1,n+1):
    #     dp[i] = dp[i-1] + dp[i-2]

    # -=----- sopt ---------------------------

    curr = 1
    prev = 0
    for i in range(1,n+1):
        res = curr + prev
        prev = curr
        curr = res


    return curr


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def printLL(head):
    if head == None:
        return
    
    pt = head
    while(pt!=None):
        print(pt.val)
        pt = pt.next


def solve7(head):
    if head == None:
        return head
    
    pt = head
    b = head.next

    while(pt.next != None and b != None):
        
        if(pt.val == b.val):
            pt.next = b.next
            b = pt
        else:
            pt = pt.next
        
        b = b.next
        
    return head


head = ListNode(1)
head.next = ListNode(1,ListNode(2,ListNode(3,ListNode(3))))

head = solve7(head)
printLL(head)