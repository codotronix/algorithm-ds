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


arr = [2,1,4,2,3,7,8,4,0,9,6]

print("\n**********************************\n")
print("Will Bubble-Sort this array: ")
print(arr)
print("\n**********************************\n")
print("Resulting array: ")
print(bubbleSort(arr))
print("\n**********************************\n")

print(arr)
