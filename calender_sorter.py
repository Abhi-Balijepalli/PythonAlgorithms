# Author: Abhi Balijepalli
# Name: CS325 Assignment 3 - Q3
# Description: Take in two arguments the first argument would be the number of tasks and the second argument would be a list of activities. 
#              Each activity would have an activity number, start time and finish time.

def activity_selection(n, activities):
    rows = n
    fList = []
    sList = []
    for i in range(n):      # i am taking the start times, and finish times and sorting them into an array. 
        fList.append(activities[i][2])
        sList.append(activities[i][1])
    print_activity_selection(sList,fList)   # they are getting passed into the the actual greedy algorithm

def print_activity_selection(s,f):
    n = len(f)
    select = []
    count = 1
    i = 0
    select.append(1)   #i made the greedy choice of taking the first activity always, technically this is effcient as well because that was another type of optimal solution.
    for j in range(n):
        if s[j] >= f[i]: #compares the start times with finish times and if it's greater or equal it will append that element number + 1 (becuase arr start at 0)
            select.append(j + 1)
            count +=1
            i = j
    print("Number of activties: ", count)
    print ("Activities: ", select)

if __name__ == "__main__":
    print("given test case: ")
    activity_selection(11, [[1, 1, 4], [2, 3, 5], [3, 0, 6], [4, 5, 7], [5, 3, 9], [6, 5, 9],[7, 6, 10], [ 8, 8, 11], [ 9, 8, 12], [10, 2, 14], [11, 12, 16]] )
    
    print("--------")
    print("These are my test cases: ")
    activity_selection(5, [[1,1,4],[2,3,5],[3,3,7],[4,5,8],[5,8,10]])
    print("")
    activity_selection(7, [[1,2,3],[2,3,5],[3,4,7],[4,5,7],[5,7,10],[6,9,13], [7,8,13]])