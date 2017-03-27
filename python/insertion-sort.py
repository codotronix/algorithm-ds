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


arr = [2,1,4,2,3,7,8,4,0,9,6]

print("\n**********************************\n")
print("Will Insertion-Sort this array: ")
print(arr)
print("\n**********************************\n")
print("Resulting array: ")
print(insertionSort(arr))
print("\n**********************************\n")
