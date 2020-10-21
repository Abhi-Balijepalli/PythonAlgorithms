# Author: Abhi Balijepalli
# Description: a function zombie_attack() which takes a 2D matrix as an argument and returns the number of  days for the whole group to be zombies.  
# Name: zombie_attack()

def zombie_attack(matrix):
    tracker = [] #tracks positions of zombies, a stack
    humans = 0
    days = 0
    explored = [[1,0],[-1,0],[0,1],[0,-1]] #two vertices are connected by an edge, they are adjacent. These are directions you can go
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[0])):
            if(matrix[i][j] == 2):
                tracker.append([i,j]) #will keep track of the zombies (coordinates)
            elif(matrix[i][j] == 1):
                humans+=1 #will count number of humans
    if humans == 0:
        return 0 # no humans then no point of algorithm
    while(tracker):
        days+=1
        for i in range(len(tracker)):
            top = tracker.pop(0) #pops out the first element from the stack
            for j in explored:
                nextElement = [top[0]+j[0], top[1]+j[1]] #coordinate system
                if (nextElement[0] >= 0 and nextElement[0] < len(matrix) and nextElement[1]>=0 and nextElement[1]<len(matrix[0])):
                    if(matrix[nextElement[0]][nextElement[1]] == 1): #basically see if they are human, then turn into zombie
                        matrix[nextElement[0]][nextElement[1]] = 2
                        humans -=1 #will try to go down to 0, if not then days will be -1
                        if(humans == 0):
                            return days
                        tracker.append(nextElement) #next coordinate in the stack    
    return -1
    





if __name__ == "__main__":
    print("----------------")
    print("Given Test Case: ")
    print("#1: ",zombie_attack( [[ 1, 2, 1, 0, 0 ],  [ 0, 0, 0, 0, 1],  [ 2, 0, 0, 0, 2], [ 0, 0, 0, 0, 0]] )) # return 1
    print("#2: ",zombie_attack( [[ 1, 2, 1, 1, 0 ],  [ 0, 0, 0, 0, 1],  [ 2, 0, 0, 0, 2], [ 0, 0, 0, 1, 1]] )) # return 2
    print("----------------")
    
    print("My Test Cases:")
    print("#1: ",zombie_attack( [[ 1, 0, 1, 0, 1 ],  [ 0, 2, 1, 0, 1],  [ 2, 1, 0, 0, 2], [ 0, 2, 0, 0, 0]] )) # humans will survive, so return -1
    print("#2: ",zombie_attack( [[ 1, 1, 1, 0, 0 ],  [ 0, 0, 2, 1, 1],  [ 2, 0, 0, 0, 1], [ 1, 0, 0, 1, 2]] )) # should give 3 days
    print("#3: ",zombie_attack( [[ 1, 2, 1, 1, 1 ],  [ 0, 1, 2, 1, 1],  [ 2, 0, 0, 0, 1], [ 1, 0, 0, 1, 1]] )) # should give 5 days