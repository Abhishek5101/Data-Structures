#!python


def linear_search(array, item):
	"""return the first index of item in array or None if item is not found"""
	# implement linear_search_iterative and linear_search_recursive below, then
	# change this to call your implementation to verify it passes all tests
	return linear_search_recursive(array, item)
	# return linear_search_iterative(array, item)


def linear_search_iterative(array, item):
	# loop over all array values until item is found
	for index, value in enumerate(array):
		if item == value:
			return index  # found
	return None  # not found


def linear_search_recursive(array, item, index=0):
	# TODO: implement linear search recursively here
	if index >= len(array):
		return None
	for index, value in enumerate(array):
		if item == value:
			return index  # found
	return linear_search_recursive(array, item, index+1)  # not found
	# once implemented, change linear_search to call linear_search_recursive
	# to verify that your recursive implementation passes all tests


def binary_search(array, item):
	"""return the index of item in sorted array or None if item is not found"""
	# implement binary_search_iterative and binary_search_recursive below, then
	# change this to call your implementation to verify it passes all tests
	return binary_search_recursive(array, item, 0, len(array)-1)
	# return binary_search_iterative(array, item)


def binary_search_iterative(array, item):
	# TODO: implement binary search iteratively here
	array = sorted(array)
	low = 0
	high = len(array) - 1
	while low <= high:
		mid = (low + high)//2
		if array[mid] == item:
			return mid
		elif array[mid] < item:
			low = mid + 1
		elif array[mid] > item:
			high = mid - 1
	return None
	# once implemented, change binary_search to call binary_search_iterative
	# to verify that your iterative implementation passes all tests


def binary_search_recursive(array, item, left=None, right=None):
	# TODO: implement binary search recursively here
	array = sorted(array)
	mid = (left + right)//2
	if left > right:
		return None
	if array[mid] == item:
		return mid
	elif array[mid] < item:
		return binary_search_recursive(array, item, mid+1, right)
	elif array[mid] > item:
		return binary_search_recursive(array, item, left, mid-1)

# once implemented, change binary_search to call binary_search_recursive
	# to verify that your recursive implementation passes all tests
