def heapify(arr,rootNode):
	child1 = -1 if (2*rootNode > len(arr)) else 2*rootNode
	child2 = -1 if (2*rootNode+1 > len(arr)) else 2*rootNode+1

	# case 1: if both the children present
	if child1 != -1 and child2 != -1:
		# if already heaped just return
		if arr[rootNode-1] >= arr[child1-1] and arr[rootNode-1] >= arr[child2-1]:
			return
		else:
			# see who is bigger b/n child1 and child2
			bigger = ''
			if arr[child1-1] >= arr[child2-1]:
				bigger = child1
			else:
				bigger = child2
			
			temp = arr[rootNode-1]
			arr[rootNode-1] = arr[bigger-1]
			arr[bigger-1] = temp

			#heapify(arr, child1)
			#heapify(arr, child2)


	# case 2: only left child present
	elif child1 != -1:
		if arr[child1-1] > arr[rootNode-1]:
			temp = arr[rootNode-1]
			arr[rootNode-1] = arr[child1-1]
			arr[child1-1] = temp
			#heapify(arr, child1)

	# case 3: only right child present
	elif child2 != -1:
		if arr[child2-1] > arr[rootNode-1]:
			temp = arr[rootNode-1]
			arr[rootNode-1] = arr[child2-1]
			arr[child2-1] = temp
			#heapify(arr, child2)



def correct_heap(arr, root):
	swapNode = ''
	# if both children present
	if (2*root) <= len(arr) and (2*root+1) <= len(arr):
		if(arr[2*root-1] >= arr[2*root+1-1]):
			swapNode = 2*root
		else:
			swapNode = 2*root + 1

	# if only left child present
	elif (2*root) <= len(arr):
		swapNode = 2*root

	# if only right child present
	elif (2*root+1) <= len(arr):
		swapNode = 2*root + 1

	#Swap root with swapNode
	temp = arr[root-1]
	arr[root-1] = arr[swapNode-1]
	arr[swapNode-1] = temp



def heap_check(arr):
	i = 1
	while(i <= len(arr)):
		if (2*i <= len(arr) and arr[i-1] < arr[2*i-1]) or (2*i+1 <= len(arr) and arr[i-1] < arr[2*i+1-1]):
			correct_heap(arr, i)
			# recheck from begining
			# print(arr)
			i=1
		else:
			i += 1
			
a = [2, 3, 5, 4, 6, 9, 7, 4]

print(a)

heap_check(a)

print(a)