'''

Problem: FIZZBUZZ 

*** INSTRUCTIONS *************************************************
Given an input, print all numbers up to and including that input, unless they are divisible by 3, then print "fizz" instead, or if they are divisible by 5, print "buzz". If the number is divisible by both, print "fizzbuzz".


*** TEST CASES *************************************************
For example, given 5:
1
2
fizz
4
buzz


Given 10:
1
2
fizz
4
buzz
fizz
7
8
fizz
buzz

'''

def fizzbuzz(n):
  for i in range(1, n+1):
    if i % 3 == 0 and i % 5 == 0:
      print("fizzbuzz")
    elif i % 3 == 0:
      print("fizz")
    elif i % 5 == 0:
      print("buzz")
    else:
      print(i)
    
# Ask user for number
test_case = int(input("Please enter an input number:"))
fizzbuzz(test_case)
