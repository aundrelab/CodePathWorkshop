'''

Problem: Power of Three
Source: Leetcode
Link: https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/745/


*** Prompt *************************************************
Given an integer, write a function to determine if it is a power of three.


*** Testcases/Examples *************************************************

Example 1:
Input: 27
Output: true

Example 2:
Input: 0
Output: false

Example 3:
Input: 9
Output: true

Example 4:
Input: 45
Output: false

'''


def power_of_three(n):
  for i in range(n+1):
    if 3 ** i == n:
      return True
  return False


''' 
*** TESTING ****************************************************
'''

# Test 1
# Input: 9
# Ouput: true
print(power_of_three(9))

# Test 2
# Input: 45
# Output: false
print(power_of_three(45))
