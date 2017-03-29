/*
* This function will correct only 1 heap starting from given rootNode
*/
function correctHeap(arr, root) {
	var swapIndex = 0;

	//if both the children are present
	if (2*root <= arr.length && 2*root+1 <= arr.length) {
		//root must be swapped with bigger child
		swapIndex = (arr[2*root - 1] >= arr[2*root + 1 - 1]) ? 2*root : 2*root + 1;
	}
	//only left child present 
	else if (2*root <= arr.length) {
		swapIndex = 2*root;
	}
	//only right child is present
	else if (2*root+1 <= arr.length) {
		swapIndex = 2*root + 1;
	}

	//swap the values
	temp = arr[swapIndex-1];
	arr[swapIndex-1] = arr[root-1];
	arr[root-1] = temp;
}


function checkHeap (arr) {
	var i = 1;

	while (i <= arr.length) {
		//treat i as root and check if there is any violation of heap
		if ((2*i <= arr.length && arr[2*i-1] > arr[i-1]) || 
			(2*i+1 <= arr.length && arr[2*i+1-1] > arr[i-1])) {

			//correct the violation
			correctHeap(arr, i);

			//reset the index so that it again checks from top
			i = 1;
		}
		//No violation found
		else {
			i++;
		}
	}

	console.log(arr);
}

