
def swap(nums,i,j):

    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp


def stringPermutation(nums:list[int], index:int ,res):
    if (index == len(nums)):
        res.append(nums[:])
        return
    
    for j in range(index,len(nums)):
       
        nums[j], nums[index] = nums[index], nums[j]
        print(nums)
        stringPermutation(nums,index+1,res)

        # backtrack
        nums[j], nums[index] = nums[index], nums[j]




nums = [1,2,3]

res = []

stringPermutation(nums,0,res)

print(res)
