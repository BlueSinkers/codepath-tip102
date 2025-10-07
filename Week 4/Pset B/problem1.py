"""
Questions I would ask:
1. can a task pair with itself? 
2. what if no pair adds up exactly?
3. can the list be empty

Plan in plain english:
use a set to keep track of seen task times. loop through each task, calculate complement needed for available time, if complement in set return True, otherwise add task to set. return False if no pair found
"""

def find_task_pair(task_times, available_time):
 seen = set()
 for t in task_times:
  comp = available_time - t
  if comp in seen: return True
  seen.add(t)
 return False

task_times = [30,45,60,90,120]
available_time = 105
print(find_task_pair(task_times,available_time))

task_times_2 = [15,25,35,45,55]
available_time = 100
print(find_task_pair(task_times_2,available_time))

task_times_3 = [20,30,50,70]
available_time = 60
print(find_task_pair(task_times_3,available_time))

#time complexity: O(n)
#space complexity: O(n)
