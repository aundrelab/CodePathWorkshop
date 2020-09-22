
'''
*** Problem ****************************************************
Problem: Pascals Triangle
Source: InterviewBit
Link: https://www.interviewbit.com/problems/pascal-triangle/

*** Prompt ****************************************************

Given numRows, generate the first numRows of Pascal’s triangle.

Pascal’s triangle : To generate a given row in Pascal's Triangle (we'll call it R):
for R[i] in row R, sum up R[i] and R[i-1] from previous row R - 1.

*** Examples ****************************************************

Given numRows = 5,
Return
[
     [1],
     [1,1],
     [1,2,1],
     [1,3,3,1],
     [1,4,6,4,1]
]

'''

# *** Solution *****************************************************

def pascal_triangle(numRows):
  # start at 1 in for loop because in pascals, the row always begins with 1
  # so we don't need to do anything with first index
  pascals = [[1] * i for i in range(1, numRows+1)]
  for x in range(2, len(pascals)):
    for y in range(1, len(pascals[x])-1):
      pascals[x][y] = pascals[x-1][y] + pascals[x-1][y-1]
  return pascals


'''
*** TESTING ****************************************************
'''

'''
Test 1
Input: 5
Ouput:
[
     [1],
     [1,1],
     [1,2,1],
     [1,3,3,1],
     [1,4,6,4,1]
]
''' 
print(pascal_triangle(5))

