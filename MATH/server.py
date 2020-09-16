'''

Problem: Server 
Source: Kattis
Link: https://open.kattis.com/problems/server

*** Prompt *************************************************
You are in charge of a server that needs to run some submitted tasks on a first-come, first-served basis. Each day, you can dedicate the server to run these tasks for at most T minutes. Given the time each task takes, you want to know how many of them will be finished today.


*** Example *************************************************
Consider the following example:

Assume T=180 and the tasks take 45, 30, 55, 20, 80 and 20 minutes (in the order that they are submitted). Then, only four tasks can be completed. The first four tasks can be completed because they take 150 minutes, but not the first five, because they take 230 minutes which is greater than 180. Notice that although there is enough time to perform the sixth task (which takes 20 minutes) after completing the fourth task, you cannot do that because the fifth task is not done yet.


*** Input *************************************************
The input consists of a two lines. 

The first line contains two integers n and T.
1 ≤ n ≤ 50 is the number of tasks 
1 ≤ T ≤ 500 is the total amount of execution time available. 

The second line contains n positive integers, separated by spaces, smaller than 100, indicating how long each task takes in order they are submitted (the same order they must be evaluated in).
1 < n < 100 - the input looks like this:
n n n n n 

*** Output *************************************************
Display (by printing) the number of tasks that can be completed in T minutes on a first-come, first-served basis.


*** My UMPIRE Method **********************************************
## Input:
2 lines
data type: string
 Line 1: two integers n and T
          - n: the number of tasks
           - T: the total amount of execution time available
 Line 2: amount of time per task for n times
           - from 1 to n, the amount of min per task
 ## Desired Output:
 1 line of output:
   - data type: integer
   - the amount of tasks they are able to complete in order
 ## Example Walkthrough
 input: 4 85
       20 60 10 5
 20 <= 85 True (task 1)
 20 + 60 = 80
 80 <= 85 True (task 1 and task 2)
 80 + 10 = 90
 90 <= 85 False (break/stop)
 conc: only task 1 and task 2 can be completed in the amount of execution time given
 output: 2 
       - 20 + 60 <= 85 but 20 + 60 + 10 > 85 (therefore it is 2)
 ## Pseudocode/Steps:
 server_time_check function takes in both lines of input in the form of a string
 first parameter is the two ints: n and T
 - use .split() to retrieve the values separately
     - convert these values into integers
 - keep track of both the number of tasks and total amount of time using variables
 second parameter is the line of time it takes to complete each task
 - use .split() to convert the string and put the values in a separately list
 - create a sum variable to keep track of the amount of time being taken completing the tasks
 - loop through list/array 

 functions/methods:
   - split()
   - enumerate() --> to retrieve amount of tasks, instead of having a count variable
'''


def server_time_check(task_config, task_times):
  n = int(task_config.split(" ")[0]) # retrieves n number of tasks
  t = int(task_config.split(" ")[1]) # stores total amount of time 
  taskTimes = task_times.split(" ") # creates list of task times
  availableTimeSum = 0 # check times -- the sum
  for i, time in enumerate(taskTimes):
    availableTimeSum += int(time)
    if(availableTimeSum > t):
      return i
  return len(taskTimes)


task_config = input("Please input the number of tasks, and the maximum total execution time:")
task_times = input("Please input the execution times of each task, seperated with a space:")
print(server_time_check(task_config, task_times))


''' 
*** TESTING ****************************************************

--- Test 1 ---
Input:
  6  180
  45  30  55  20  80  20

Output:
  4

--- Test 2 ---
Input:
  40  60
  20  7  10  8  10  27  2  3  10  5

Output:
  5
'''

