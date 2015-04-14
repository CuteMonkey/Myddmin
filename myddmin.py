import sys
from mytest import test
from mysplit import split

PASS = 'PASS'
FAIL = 'FAIL'
UNRESOLVED = 'UNRESOLVED'

def listminus(old_list, id):
	new_list = []
	for element in old_list:
		if element[0] != id:
			new_list.append(element)
	return new_list
	
def list_to_file(input_list, file_path):
	f = open(file_path, 'w')
	for element in input_list:
		f.write(element[1])
	f.close()
	
def list_to_string(input_list):
	s = ''
	for element in input_list:
		s += element[1]
	return s

def ddmin(test_input):
	'''Implement of delta debugging for simplifying TEST_INPUT.'''
	
	n = 2
	count = 1 #debug
	while len(test_input) >= 2:
		subsets = split(test_input, n)
		
		some_complement_is_falling = False
		for i in range(0, len(subsets)):
			complement = listminus(subsets, i)
			list_to_file(complement, simple_xml_file_path)
			#print('>>', count, i, test(xml_parser_path, simple_xml_file_path)) #debug
			
			if test(xml_parser_path, simple_xml_file_path) == FAIL:
				#--debug--
				another_path = simple_xml_file_path[:-4] + str(count) + '.xml'
				list_to_file(complement, another_path)
				#--debug--
				
				test_input = list_to_string(complement)
				n = max(n - 1, 2)
				some_complement_is_falling = True
				break
			
		if not some_complement_is_falling:
			if n == len(test_input):
				break
			n = min(n * 2, len(test_input))
		count += 1 #debug
	return complement
		

global xml_parser_path
xml_parser_path = sys.argv[1]
xml_file_path = sys.argv[2]
global simple_xml_file_path
simple_xml_file_path = xml_file_path[:-4] + '_simple.xml'

xml_file = open(xml_file_path)
input_string = xml_file.read()
xml_file.close()
min_list = ddmin(input_string)
list_to_file(min_list, simple_xml_file_path)
