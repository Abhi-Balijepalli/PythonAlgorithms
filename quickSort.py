# Author: Abhijith balijepalli
# Description: Implementing quick select.

import random
def quickPre(k, arr) :
    left = 0
    right = len(arr) - 1
    n = k-1 #this is important!
    def quickSelect(arr, left,right,k):
        if left == right:
            return arr[left]
        p = random.randint(left,right) # random pivot element in arr
        pivotIndex = partition(arr, p, left, right) #to find partition, pass the random pivot in here
        
        if n == pivotIndex:
            return arr[pivotIndex]
        elif n < pivotIndex:
            return quickSelect(arr, left, pivotIndex - 1, k) #from A[1...r-1], k
        else:
            return quickSelect(arr, pivotIndex+1, right, k) #from A[r+1...n], k-r
    if arr is None:
        return None
    return quickSelect(arr, 0 , len(arr)-1, k) #idk why this is here, but it works!

#decided to make it more modular so i did this
def partition(arr, p, left, right):
    pivot = arr[p] #the pivot number
    arr[p], arr[right] = arr[right], arr[p]
    l = left #<<#items < pivot>> i'm assuming based on the textbook notes
    for i in range(left,right):
        if arr[i] < pivot:
            arr[l], arr[i] = arr[i], arr[l] #swap A[l] <-> A[i]
            l += 1
    arr[right], arr[l] = arr[l],arr[right]
    return l
   
def main():
    print("-------------")
    print("Given test cases:")
    print(quickPre(2,[1,2,3,4,5,6]))
    print(quickPre(3,[2,6,7,1,3,5]))
    print("-------------")
    print("The following answers are my test cases:")
    print(quickPre(5,[9,6,2,3,4,5])) #this is my test function
    print(quickPre(2,[8,6,2,1,4,5,10]))
    print(quickPre(6,[8,7,2,3,6,5,9]))

if __name__ == "__main__" :
   main()