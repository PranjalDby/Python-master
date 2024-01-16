from itertools import combinations
from itertools import chain

def subsets(arr:list[int])->list[list[int]]:
    return chain.from_iterable(combinations(arr,r) for r in range(len(arr) +1))




def recursiveSubset(i,nums,res,curr)->list[list[int]]:
    if i == len(nums):
        # We reached to the end of our nums
        res.append(curr)
        return res

    # this recursive call represents choosing the current element at index i and appending it to the current subset list
    
    recursiveSubset(i+1,nums,res,curr + [nums[i]])

    # Second call is to not choose the current element

    recursiveSubset(i+1,nums,res,curr)

    return res

def stringSubsequence(i,string,res,curr)->list[list[str]]:
    if i == len(string):
        res.append(curr)
        return res
    
    #this recursive call represents choosing the current element at index i and appending it to the current subset list
    stringSubsequence(i+1,string,res,curr + [string[i]])

    # Excluding the current element
    stringSubsequence(i+1,string,res,curr)

    return res

# arr = [1,2,3,4]

# print(recursiveSubset(0,arr,[],[]))

s = "abc"

print(stringSubsequence(0,s,[],[]))