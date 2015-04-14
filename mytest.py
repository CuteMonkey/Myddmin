import os, re, sys

#for debug
DEBUG_MODE = False

def test(xml_parser_path, xml_file_path):
	'''Catch and return the execution result of XML parser.'''
	
	cmd = 'python ' + str(xml_parser_path) + ' ' + str(xml_file_path)
	exe_file = os.popen(cmd)
	
	exe_stdout_line = ''
	is_parse_complete = False
	while True:
		exe_stdout_line = exe_file.readline()
		if exe_stdout_line == '':
			break
		parse_result = re.match('Parse complete, (\d+) error\(s\)' ,exe_stdout_line)
		if parse_result != None:
			is_parse_complete = True
			err_n = int(parse_result.group(1))
			break
	exe_file.close()
	
	test_result = ''
	if is_parse_complete:
		if err_n == 0:
			test_result = 'PASS'
		else:
			test_result = 'UNRESOLVED'
	else:
		test_result = 'FAIL'
	return test_result

if DEBUG_MODE:
	print(test(sys.argv[1], sys.argv[2]))
