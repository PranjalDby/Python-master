def keypad(digits:str, i:int ,ans:list[str], curr:str, mapping):
    # base case

    if i >= len(digits):
        ans.append(curr)
        return
    
    # including the current element
    number = int(digits[i])

    value = mapping[number]

    for m in range(0,len(value)):
        curr += value[m]
        print(curr)
        keypad(digits, i+1, ans, curr, mapping)
        # removing the curr element: backtrack
        curr = curr.replace(value[m],'')


def helper(string,mapping)->list[str]:
    if len(string) == 0:
        return []
    
    ans = []
    keypad(string,0,ans,"",mapping)
    return ans


mapping = [
    "",
    "",
    "abc",
    "def",
    "ghi",
    "jkl",
    "mno",
    "pqrs",
    "tuv",
    "wxyz",
]

print(helper("36",mapping))