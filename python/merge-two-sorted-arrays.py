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


a = [1,5,8,9]
b = [2,3,4,6,7]

print("\n**********************************\n")
print("Will merge these 2 sorted arrays: ")
print(a)
print(b)
print("\n**********************************\n")
print("Resulting array is: ")
c = mergeSortedArrays(a,b)
print(c)
print("\n**********************************\n")