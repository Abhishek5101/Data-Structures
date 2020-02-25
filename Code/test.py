def contains(text, pattern):
	"""Return a boolean indicating whether pattern occurs in text."""
	assert isinstance(text, str), 'text is not a string: {}'.format(text)
	assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
	# TODO: Implement contains here (iteratively and/or recursively)
	if pattern == '':
		return True
	# for index in range(len(pattern)-1):
	# 	for jindex in range(len(text)-1):
	# 		if pattern[index] == text[jindex]:
	# 			index += 1
	# 			jindex += 1
	# 	else:
	# 		return True
	# return False
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
				return True
		
		else:  # unmatch
			start += 1
			j = 0
			i = start
			
	
	return False

word = 'abc'
pattern = 'b'
print(contains(word, pattern))