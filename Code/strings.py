#!python


def contains(text, pattern):
	"""Return a boolean indicating whether pattern occurs in text."""
	assert isinstance(text, str), 'text is not a string: {}'.format(text)
	assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
	# TODO: Implement contains here (iteratively and/or recursively)
	"""
	Time Complexity O(n*b)---> The length of the text and for each character check if it is a match(b)
	Space Complexity O(1)
	"""
	if pattern == '':
		return True
	
	index = find_index(text, pattern)
	return True if index is not None else False


def find_index(text, pattern):
	"""Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
	assert isinstance(text, str), 'text is not a string: {}'.format(text)
	assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
	# TODO: Implement find_index here (iteratively and/or recursively)
	"""
	Time Complexity O(n*b)---> The length of the text and for each character check if it is a match(b)
	Space Complexity O(1)
	"""

	if pattern == '':
		return 0
	
	i, j, start = 0, 0, 0
	while i < len(text):
		print(f"outside -> i: {i}, j: {j}")
		if text[i] == pattern[j]:  # first match
			# start = i
			print(f"i: {i}, j: {j}")
			j += 1
			i += 1
			
			if j == len(pattern):
				print(f"start: {start}")
				return start
		
		else:  # unmatch
			start += 1
			j = 0
			i = start
	
	return None
	
def find_all_indexes(text, pattern):
	"""Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
	assert isinstance(text, str), 'text is not a string: {}'.format(text)
	assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
	# TODO: Implement find_all_indexes here (iteratively and/or recursively)
	"""
	Time Complexity O(n*b)---> The length of the text and for each character check if it is a match(b)
	Space Complexity O(n)--> for the new array created to store matching indices
	"""
	
	indexes = []
	
	if pattern == '':
		for i in range(len(text)):
			indexes.append(i)
		return indexes
	
	index = find_index(text, pattern)
	
	if index is not None:
		indexes.append(index)
		index = index + 1
		j = 0
		start = index
		
		while index < len(text):
			print(f"outside -> i: {index}, j: {j}")
			if text[index] == pattern[j]:  # first match
				# start = i
				print(f"i: {index}, j: {j}")
				j += 1
				index += 1
				
				if j == len(pattern):
					print(f"start: {start}")
					# return start
					indexes.append(start)
					start += 1
					j = 0
					index = start
			else:  # unmatch
				start += 1
				j = 0
				index = start
		
		return indexes
	
	return indexes  # not found


def test_string_algorithms(text, pattern):
	found = contains(text, pattern)
	print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
	# TODO: Uncomment these lines after you implement find_index
	index = find_index(text, pattern)
	print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
	# TODO: Uncomment these lines after you implement find_all_indexes
	indexes = find_all_indexes(text, pattern)
	print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
	"""Read command-line arguments and test string searching algorithms."""
	import sys
	args = sys.argv[1:]  # Ignore script file name
	if len(args) == 2:
		text = args[0]
		pattern = args[1]
		test_string_algorithms(text, pattern)
	else:
		script = sys.argv[0]
		print('Usage: {} text pattern'.format(script))
		print('Searches for occurrences of pattern in text')
		print("\nExample: {} 'abra cadabra' 'abra'".format(script))
		print("contains('abra cadabra', 'abra') => True")
		print("find_index('abra cadabra', 'abra') => 0")
		print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
	main()
