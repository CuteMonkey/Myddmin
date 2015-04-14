def split(test_input, n):
	'''Split the input stirng TEST_INPUT into N subsets;
	return the list of subsets with id'''
		
	test_len = len(test_input)
	subset_len = test_len // n
	remainder_len = test_len % n
	start_index = 0
	
	subsets = []
	substring = ''
	for i in range(0, n):
		if i < remainder_len:
			substring = test_input[start_index:(start_index + subset_len + 1)]
		else:
			substring = test_input[start_index:(start_index + subset_len)]
		tup = (i, substring)
		subsets.append(tup)
		start_index += len(substring)
	
	return subsets
