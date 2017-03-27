import time

####################################
# BUBBLE SORT
####################################
def bubbleSort(a):
	i=0
	lenA = len(a)
	
	while i < lenA:
		j = 1
		while j < (lenA - i):
			if(a[j] < a[j-1]):
				temp = a[j]
				a[j] = a[j-1]
				a[j-1] = temp
			j += 1
		i += 1

	return a
####################################


####################################
# INSERTION SORT
####################################
def insertionSort(a):
	i = 1	

	while i < len(a):
		key = a[i]
		j = i-1

		while j >= 0:
			if (a[j] > key):
				a[j+1] = a[j]
				j -= 1
			else:
				break			

		a[j+1] = key
		i += 1

	return a
####################################


####################################
# MERGE SORT
####################################
def mergeSortedArrays (a,b):
	ai = 0		# index of array a
	bi = 0		# index of array b
	res = []

	while ai < len(a) and bi < len(b):
		if a[ai] < b[bi]:
			res.append(a[ai])
			ai = ai + 1
		else:
			res.append(b[bi])
			bi = bi + 1

	while ai < len(a):
		res.append(a[ai])
		ai = ai + 1

	while bi < len(b):
		res.append(b[bi])
		bi = bi + 1

	return res

def mergeSort(arr):
	if len(arr) == 1:
		return arr
	else:
		mid = round(len(arr)/2)
		a = mergeSort(arr[0:mid])
		b = mergeSort(arr[mid:])
		c = mergeSortedArrays(a,b)
		return c
####################################


#######################################
# Create an list of Descending numbers
#######################################
def createData(length):
	length -= 1	#since we will also include 0
	data = []

	while length >= 0:
		data.append(length)
		length -= 1

	return data
#######################################

def startTest():
	dataLength = 1000
	a = createData(dataLength)

	print("")
	print("********************************************************")
	print("Starting comparison test with dataLength = " + str(dataLength))
	print("********************************************************")
	print("")
	
	t1 = int(round(time.time() * 1000))
	mrg = mergeSort(a[:])
	t2 = int(round(time.time() * 1000))
	print("Merge Sort took " + str(t2-t1) + "ms")
	print("")

	t1 = int(round(time.time() * 1000))
	ins = insertionSort(a[:])
	t2 = int(round(time.time() * 1000))
	print("Insertion Sort took " + str(t2-t1) + "ms")
	print("")

	t1 = int(round(time.time() * 1000))
	bbl = bubbleSort(a[:])
	t2 = int(round(time.time() * 1000))
	print("Bubble Sort took " + str(t2-t1) + "ms")
	print("")

startTest()