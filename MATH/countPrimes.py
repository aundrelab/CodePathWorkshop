'''

Prompt:
Count the number of prime numbers less than a non-negative number, n.

Given 10, your countPrimes solution should return 4
Given 20, your countPrimes solution should return 8

1 does not count as a prime number.

'''


############
# Solution #
############

# Determine if the input number is prime 
def isPrime(n):
  for current_number in range(2,n):
    # if the input number is evenly divisible by the current number?
    if n % current_number == 0:
      return False
  return True

# Determine how many prime numbers are UNDER the input number
def countPrimes(n):
  count = 0
  for i in range(2, n):
    if isPrime(i) == True:
      count += 1
  return count


###########
# Testing #
###########

# Test 1 
# Expected Result: 9
print(countPrimes(25))

# Test 2
# Expected Result: 18
print(countPrimes(64))

# Test 3
# Expected Result: 30
print(countPrimes(125))
