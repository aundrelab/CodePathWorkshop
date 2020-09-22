
'''
*** Problem ****************************************************
Problem: Wave Array
Source: InterviewBit
Link: https://www.interviewbit.com/problems/wave-array/

*** Prompt ****************************************************

Given an array of integers, sort the array into a wave like array and return it, 
In other words, arrange the elements into a sequence such that a[1] >= a[2] <= a[3] >= a[4] <= a[5] ...

*** Examples ****************************************************

Given [1, 2, 3, 4]

One possible answer : [2, 1, 4, 3]
Another possible answer : [4, 1, 3, 2]

'''

# *** Solution *****************************************************

def wave_array(integers):
  integers = sorted(integers)
  for i in range(0, len(integers)-1, 2):
    integers[i], integers[i+1] = integers[i+1], integers[i]
  return integers

'''
*** TESTING ****************************************************
'''

'''
Test 1
Input: [1, 2, 3, 4]
Ouput:
  [2, 1, 4, 3]
  or
  [4, 1, 3, 2]
''' 
print(wave_array([1, 2, 3, 4]))

