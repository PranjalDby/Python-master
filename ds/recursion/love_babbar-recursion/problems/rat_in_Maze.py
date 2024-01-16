def isSafe(row,col,n,visited,maze)->bool:
    #checking if row is in bound and column is in bound

    if (row>=0 and row < n) and (col >=0 and col < n) and visited[row][col] == 0 and maze[row][col] == 1:
        return True
    
    else:
        return False


def ratInsideMaze(maze,row,col,res,visited,path:str):

    # Base case
    if row == len(maze)-1 and col == len(maze)-1:
        res.append(path)
        return
    
    visited[row][col] = 1

    #down
    newRow = row + 1
    newCol = col

    if isSafe(newRow,newCol,len(maze),visited,maze):
        path += 'D'
        ratInsideMaze(maze,newRow,newCol,res,visited,path)
        path = path[:len(path)-1]

    # left
    
    newRow = row
    newCol = col-1

    if isSafe(newRow,newCol,len(maze),visited,maze):
        path += 'L'
        ratInsideMaze(maze,newRow,newCol,res,visited,path)
        path = path[:len(path)-1]

    #right
    newRow = row
    newCol = col +  1
    if isSafe(newRow,newCol,len(maze),visited,maze):
        path += 'R'
        ratInsideMaze(maze,newRow,newCol,res,visited,path)
        path = path[:len(path)-1]
    
    #Up
    newRow = row-1
    newCol = col
    if isSafe(newRow,newCol,len(maze),visited,maze):
        path += 'U'
        ratInsideMaze(maze,newRow,newCol,res,visited,path)
        path = path[:len(path)-1]

    
    # Backtrackly remove the visited flag for current position
    
    visited[row][col] = 0



from unicodedata import *

def helper(maze)->list[str]:

    res = []
    # for travelling in the maze
    if maze[0][0] == 0:
        return res
    
    visited = [[0 for x in range(len(maze))] for k in range(len(maze))]
   
    ratInsideMaze(maze,0,0,res,visited,"")


    return sorted(res,key=lambda x : ord(x[0]) > ord(x[len(x)-1]))
    


maze = [
    [1,0,0,0],
    [1,1,0,1],
    [1,1,0,0],
    [0,1,1,1],
]
s = "DDRRRD"
s = s[:len(s)-1]
s = s[:len(s)-1]
print(s)
print(helper(maze))