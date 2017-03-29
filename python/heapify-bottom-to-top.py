def heap_check(arr):
	#we will start journey from last node
	n = len(arr)

	while(n > 0):
		parentNode = int(n/2)

		#if no parent node, then we are done
		if parentNode < 1:
			break

		# if this node is greater than parent, swap
		if arr[n-1] > arr[parentNode-1]:
			temp = arr[n-1]
			arr[n-1] = arr[parentNode-1]
			arr[parentNode-1] = temp
			#reset n
			n = len(arr)

		n -= 1


a = [2, 3, 5, 4, 6, 9, 7, 4]

print(a)

heap_check(a)

print(a)
