
'''
*** Problem ****************************************************
Problem: Rotated Array (Similar)
Source: InterviewBit
Link: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/646/

*** Prompt ****************************************************

Given an array, rotate the array to the right by k steps, where k is non-negative.


*** Examples ****************************************************

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

'''

# *** Solution *****************************************************

def rotate_array(input_array, k):
  for i in range(k):
    input_array.insert(0, input_array.pop())
  print(input_array)


'''
*** TESTING ****************************************************
'''

# Test 1
# Input: 
#   [1,2,3,4,5,6,7], 3
# Ouput: [5,6,7,1,2,3,4]
print(rotate_array([1,2,3,4,5,6,7], 3))

# Test 2
# Input: 
#   [3,99,-1,-100], 2
# Output: [3,99,-1,-100]
print(rotate_array([3,99,-1,-100], 2))


