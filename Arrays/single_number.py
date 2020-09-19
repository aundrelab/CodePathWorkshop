'''

Problem: Single Number
Source: LeetCode
Link: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/549/

*** Prompt *************************************************

Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?


*** Testcases/Examples *************************************************

Example 1:
Input: [2,2,1]
Output: 1

Example 2:
Input: [4,1,2,1,2]
Output: 4


*** Solution *****************************************************
'''

def single_number(integers):
  for i in integers:
    if integers.count(i) == 1:
      return i
  

''' 
*** TESTING ****************************************************
'''

# Test 1
# Input: [2,2,1]
# Ouput: 1
print(single_number([2,2,1]))

# Test 2
# Input: [4,1,2,1,2]
# Output: 4
print(single_number([4,1,2,1,2]))
