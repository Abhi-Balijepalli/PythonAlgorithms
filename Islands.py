# Author: Abhi Balijepalli
# Description: You are given a 2D matrix which represents a map. 
# The ‘1’s in the matrix represents land and ‘0’ s represent water. Count the number of  islands in the map. 
# An island is a sequence of  ones connected either vertically or horizontally. 
# Name: Islands.py - DFS Traversals

def count_islands(matrix):
    islands = 0 # return the number of islands
    checker = set() #to keep track of nodes you visited
    
    if matrix is None:
        return 0
    
    for i in range(0,len(matrix)):
        for j in range (0,len(matrix[0])):
            if matrix[i][j] == 1 and (i,j) not in checker: #checker is like the (visited node or not)
                dfs(matrix, i, j, checker)
                islands += 1 #simple counter to see if the islands exist
    # print(islands)
    return islands

def dfs(matrix, row, col, explored):
    #this is to check for bounds
    if(row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[row]) or (row,col) in explored or matrix[row][col] == 0):
        return
    
    explored.add((row,col)) #this was to keep track if i have visited that node, ik it's not required since its a 2d matrix and but its important to keep this when we are on a graph.
    
    # this recrusive call, will up,down,left,right. to see if there is an island.
    dfs(matrix, row+1, col, explored)
    dfs(matrix, row-1, col, explored)
    dfs(matrix,row, col+1,explored)
    dfs(matrix,row,col-1,explored)
        

if __name__ == "__main__":
    print("----------------")

    print("Given Test Case: ")
    print("Number of islands: ", count_islands([[ 1, 1, 1, 0, 0 ], [ 0, 0, 0, 0, 1], [ 1, 0, 0, 0, 1],[ 0, 0, 0, 0, 0]]))
    
    print("----------------")
    
    print("My Test Cases:")
    print("#1, Number of islands: ", count_islands([[ 1, 0, 1, 1, 0 ], [ 0, 0, 1, 1, 0], [ 0, 0, 0, 0, 1],[ 1, 0, 0, 0, 0]])) #output should be 4
    print("#2, Number of islands: ", count_islands([[ 0, 0, 0, 0, 0 ], [ 0, 0, 0, 0, 0], [ 0, 0, 0, 0, 0],[ 0, 0, 0, 0, 0]])) #output should be 0
    print("#3, Number of islands: ", count_islands([[ 1, 0, 1, 0, 1 ], [ 1, 0, 1, 0, 1], [ 0, 1, 0, 1, 0],[ 0, 1, 0, 1, 0]])) #output should be 5
    print("#4, Number of islands: ", count_islands([[ 0, 1, 0, 1, 1 ], [ 0, 1, 0, 1, 0], [ 0, 0, 0, 0, 0],[ 0, 0, 0, 0, 1]])) #output should be 3