'''
Problem: Excel Column Number
Source: LeetCode
Link: https://leetcode.com/problems/excel-sheet-column-number/


*** Prompt *************************************************
Given a column title as appears in an Excel sheet, return its corresponding column number.


*** Testcases/Examples *************************************************
A -> 1
    
B -> 2
    
C -> 3
    
Z -> 26
    
AA -> 27
    
AB -> 28 
'''

def excel_column_to_number(column):
	value = 0
	# start at end of string
	for i in range(len(column)-1, -1, -1):
		# converts character to unicode number representation
		charVal = ord(column[i]) - 64
		# takes in account placement/index in string with 26^index representing alpha
		value += charVal * (26 ** ((len(column) - 1) - i))
	return value

''' 
*** TESTING ****************************************************
'''

# Test 1
# Input: 'A'
# Output: 1
print(excel_column_to_number('A'))

# Test 2
# Input: 'AB'
# Output: 28
print(excel_column_to_number('AB'))

# Test 3
# Input: 'ZY'
# Output: 701
print(excel_column_to_number('ZY'))

