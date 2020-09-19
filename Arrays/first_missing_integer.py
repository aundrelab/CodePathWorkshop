
'''
Problem: First Missing Integer
Source: InterviewBit
Link: https://www.interviewbit.com/problems/first-missing-integer/

Given an unsorted integer array, find the first missing positive integer.

Example:
Given [1,2,0] return 3,
[3,4,-1,1] return 2,
[-8, -7, -6] returns 1
Your algorithm should run in O(n) time.

'''

def first_missing_positive_integer(integers):
  arr = [False] * max(integers)
  # reasoning:
  # creates an array/list of the size of the maximum number and all initizalized to false
  for i in integers:
  # for every num in integer
  # it converts index at num to True 
  # ex. 1 is represented by integers[1]
  # ex. 2 is represented by integers[2]
    if i <= 0:
      continue
    elif i > 0:
      arr[i-1] = True
  for index, truth in enumerate(arr):
    if truth == False:
      return index+1
  if(all(arr)):
    return (len(arr) + 1)
  elif(len(arr) == 0):
    return 1



'''
*** TESTING ****************************************************
'''

# Test 1
# Input: [1, 2, 0]
# Ouput: 3
print(first_missing_positive_integer([1, 2, 0]))

# Test 2
# Input: [3, 4, -1, 1]
# Output: 2
print(first_missing_positive_integer([3, 4, -1, 1]))

# Test 3
# Input: [-8, -7, -6]
# Output: 1
print(first_missing_positive_integer([-8, -7, -6]))
