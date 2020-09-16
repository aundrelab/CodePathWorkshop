'''

Problem: Last Factorial Digit
Source: Kattis
Link: https://open.kattis.com/problems/lastfactorialdigit


*** Prompt *************************************************
Given a non-negative number, N, return the last digit of the factorial of N.

The factorial of N, which is written as N!, is defined as the product of all of the integers from 1 to N.


*** Testcases/Examples *************************************************
Given 3 as N, the factorial is 1 x 2 x 3 = 6
Given 6 as N, the factorial is 1 x 2 x 3 x 4 x 5 x 6 = 720
Given 9 as N, the factorial is 1 x 2 x 3 x 4 x 5 x 6 x 7 x 8 x 9 = 362,880

As you can see, the number can grow to be quite large, quite quickly.

Write a function that will return only the last digit of N!, given N.
'''

def last_factorial_digit(n):
  ans = 1
  for i in range(1, n + 1):
    ans *= i

  # *** Alternate *** #
  # convert int into string
  # ans = str(ans)
  # obtain last index of string
  # last = ans[len(ans)-1]
  # return last

  # return last digit of number by using modulo
  return ans % 10
  

''' 
*** TESTING ****************************************************
'''

# Test 1
# Input: 6
# Ouput: 720 
print(excel_column_to_number(6))

# Test 2
# Input: 9
# Output: 362880
print(last_factorial_digit(9))
