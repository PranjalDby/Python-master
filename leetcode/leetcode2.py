class TreeNode:
    def __init__(self,val,left=None,right = None) -> None:
        self.val =val
        self.left = left;
        self.right = right



def solve(r1,r2)->bool:
    if r1 == None and r2 == None:
        return True
    
    # one of the lst or lst finished first, which means it is not a mirror
    if r1 == None or r2 == None:
        return False
    
    #if node is not equal

    if r1.val != r2.val:
        return False
    
    return True and (solve(r1.left,r2.right) and solve(r1.right,r2.left))


def inorder(root):
    if not root:
        return
    
    inorder(root.left)
    print(root.val)
    inorder(root.right)


def create(root,data):
    if root == None:
        node = TreeNode(data)
        root = node
        root.height = 1
        return root
    
    if root.val > data:
        root.height +=1
        root.left = create(root.left,data)

    else:
        root.height +=1
        root.right = create(root.right,data)

    
    return root

def createBst(array):
    root = None
    for i in range(len(array)):
        if root == None:
            root = create(root,array[i])

        else:
            create(root,array[i])

    return root


def height(root):
    if root == None:
        return 0
    
    return root.height

def totalHeight(root):
    if root == None:
        return 0
    
    lst = 1 + totalHeight(root.left)
    rst = 1 + totalHeight(root.right)

    return lst if lst > rst else rst

# def getHeight(root):
#     if root == None:
#         return 0
    
#     return getHeight(root.left) - getHeight(root.right)


def getHeight(root):
    if root == None:
        return 0

    l_height = getHeight(root.left)
    print(f"L_HEIGHt >> {l_height}\n")
    right_height = getHeight(root.right)
    print(f"R_H >> {right_height}\n")

    return root.height

nums = [-10,-3,0,5,9]


# ------------------------ BS

def binarySearch(nums,target):
    s = 0
    e = len(nums)-1
    count = 0
    while(s<e):
        if nums[s] + nums[e] < target:
            count += (e-s)
            s+=1
        
        else:
            e-=1


    return count
        
    

def count_ve(grid):

    mid = 0
    count  = 0
    for i in range(len(grid)):
        x = len(grid[0])-1 # col
        while(x>=0):
            if grid[i][x] < 0:
                count += 1
            
            x -=1


    return count

def solve2(nums,target):
    nums.sort()
    s = 0
    e = len(nums)-1
    mid = s + (e-s)//2
    res = []
    while(s<=e):
        if nums[mid] == target:
            res.append(mid)
            break
        
        elif nums[mid] > target:
            e = mid-1

        else:
            s = mid + 1

        mid = s + (e -s)//2

    index  = res[0]

    i = s
    while(i<index):
        if nums[i] == target:
            res.append(i)

        i+=1

    return res

def firstOccurance(nums,target):
    s = 0
    e = len(nums)-1
    first_occ_index = -1
    while(s<=e):
        mid = s + (e-s)//2
        if nums[mid] == target:
            first_occ_index = mid
            e = mid-1

        elif nums[mid] < target:
            s = mid+1

        else:
            e = mid-1

    return first_occ_index

def last_occu(nums,target):
    s = 0
    last_ = -1
    e = len(nums)-1
    while(s<=e):
        mid = s + (e-s)//2
        if nums[mid] == target:
            last_ = mid
            s = mid + 1

        elif nums[mid] < target:
            s = mid+1
        else:
            e = mid-1

    return last_


def solve3(nums,target):
    first_ = firstOccurance(nums,target)
    last_ = last_occu(nums,target)
    res = []
    while first_ < last_:
        if nums[first_] == target:
            res.append[first_]
        
        first_ +=1
    
    return res


# nums = [-6,2,5,-2,-7,-1,3]
# nums.sort()
# grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# print(count_ve(grid))



# ----------------------------------------- sorting algorithms -------------------------------------------------------------------------------

def selectionSort(arr):
    # selection sort:minimum element ko right position par insert kar rahe hai.
    # t-c:O(n2)
    # it may or may not be stable

    # for i in range(0,len(arr)-1):
    #     mini = i;
    #     for j in range(i+1,len(arr)):
    #         if(arr[mini] > arr[j]):
    #             # update mini
    #             mini = j

    #     if arr[i] > arr[mini]:
    #         t = arr[i]
    #         arr[i] = arr[mini]
    #         arr[mini] = t


    # making it stable:we have to shift the element to the right
    for i in range(0,len(arr)-1):
        mini = i;
        for j in range(i+1,len(arr)):
            if(arr[mini] > arr[j]):
                # update mini
                mini = j

        key = arr[mini]

        # shifting to the right

        for k in range(mini,i,-1):
            arr[k] = arr[k-1]

        arr[i] = key




def bubble_sort(arr):
    # Bubble
    # place the elements into its right-positions in each rounds:comparing neighbouring elements
    # stable-sorting by default.
    # TC: best-case = O(n) or Worst-case = O(n**2)
    for i in range(0,len(arr)-1):
        is_swapped = False
        for j in range(0,len(arr)-i-1):
            if(arr[j] > arr[j+1]):
                t = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = t
                is_swapped = True

        if is_swapped == False:
            print("already swapped")
            break


def insertion_sort(arr):
    # assume our smallest element is first element of arr: and it lies in sorted part.
    smallest = arr[0];
    # for i in range(1,len(arr)):
    #     temp = arr[i]
    #     # this loops is to compare the element of unsorted part and element of sorted part and right-shift
    #     index = 0;
    #     for j in range(i-1,-1,-1):
    #         index = j
    #         if arr[j] > temp:
    #             arr[j+1] = arr[j]
    #         else:
    #             break
                
    #     arr[index+1] = temp

    # using while loop
    i = 1
    while i < len(arr):
        j = i-1
        temp = arr[i]
        while j <=0:
            if arr[j] > temp:
                # right-shift
                arr[j+1] = arr[j]
                j-=1
            else:
                break
        
        arr[j+1] = temp
        i+=1




arr = [1,2,3,4,5]
insertion_sort(arr)
print(arr)




