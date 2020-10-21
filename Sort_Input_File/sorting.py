# Author: Nag Balijepalli "Abhi"
# MergeSort - will read data.txt and sort it and put it under merge.txt
# InsertSort - will read data.txt and sort it and put it under insert.txt

def gather():
	data = open("data.txt")

	file1 = open('insert.txt', 'w') #create insert.txt to write to file for insertion sort
	file1.write('Insertion Sort:\n')

	file2 = open('merge.txt', 'w') #create merge.txt to write to file for merge sort
	file2.write('Merge Sort:\n')

	for line in data:
		lists = [int(i) for i in line.split()]  #each line that i am reading here will be used to make a list, making sure they are Ints
		insertionSort(lists, file1) #num will be passed into insertionSort and mergeSort
		mergeSort(lists, file2)

#this insertionSort was made using notes in class
def insertionSort(num, file):
	# this will start on the 2nd position element and end until the end of the lists - (len(arr))
	for i in range(1,len(num)):
		temp = num[i]
		j = i -1
		while(temp < num[j] and j>=0):
			num[j+1] = num[j]
			j -= 1
		num[j+1] = temp
	# print(num)
	file.write(str(num) +"\n")


#this mergeSort was made using notes in class
def mergeSort(nums,files):
	arr1 = nums[0:len(nums)//2] # start of the list to the middle
	arr2 = nums[len(nums)//2:] # middle of the lists to the end
	i,j = 1,0
	finArr = [] #empty lists for the final lists after merging
	while i < len(arr1) and j < len(arr2):
		if arr1[i] < arr2[j]:
			finArr.append(arr1[i]) #append is for adding stuff into the original lists
			i+=1
		else:
			finArr.append(arr2[j])
			j+=1
	finArr += arr1[i:]
	finArr += arr2[j:]
	return files.write(str(finArr)+"\n")

#main method
if __name__ == '__main__':
	gather()