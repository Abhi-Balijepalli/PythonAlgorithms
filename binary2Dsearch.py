# Author: Abhijith Balijepalli
# Search for an element in a 2D sorted matrix using the binary search technique.

#this will use O(m+n) instead of having the nested forloop solution shown below ~ commented
def binarySearch(target,lists):
    rows = len(lists) #need these values to calculate sizes
    cols = len(lists[0])
    rowElement = rows-1
    colsElement = 0
    outBounds = "Out of bounds"
    tups = None
    if(lists[0][0] > target or lists[rows-1][cols-1] < target): #to see if its out of bounds.
        return outBounds
    while( rowElement >= 0 and colsElement <= cols - 1):
        x = lists[rowElement][colsElement]
        if(x < target):
            colsElement+=1 #if its greater the first row, it will go up. 
        if(x > target):
            rowElement-=1 #go back down
        if(x == target):
            tups = (rowElement,colsElement) #looks i got rows and cols, switched, don't mind the variable names
            return tups

    # my O(nxm) version:
    # for row in range(0,len(lists)):
    #     for col in range(0,len(lists[row])): #it's iterating m times on every n, so its m*n
    #         if target == lists[row][col]:
    #             tup = (row,col)
    #             return tup
                

def main():
    print("-------------")
    print("given cases:")
    print(binarySearch(4,[[1,2,3],[4,5,6],[7,8,9]])) #these are given cases from the assignment.
    print(binarySearch(10,[[2, 3, 4],[5, 7, 9],[11, 12, 13],[20, 22, 24]]))
    print("-------------")
    print("The following answers are my test cases:")
    print(binarySearch(22,[[2, 4, 6],[8, 10, 12],[14, 16, 18],[20, 22, 24]]))
    print(binarySearch(12,[[3,5,6],[9,11,12],[19,21,22]]))
    print(binarySearch(100,[[2, 4, 6],[8, 10, 12],[14, 16, 18],[20, 22, 24]]))

if __name__ == "__main__":
   main()