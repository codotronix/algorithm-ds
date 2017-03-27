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


arr = [2,1,4,2,3,7,8,4,0,9,6]

print("\n**********************************\n")
print("Will Merge-Sort this array: ")
print(arr)
print("\n**********************************\n")
print("Resulting array: ")
print(mergeSort(arr))
print("\n**********************************\n")