"""
Questions I would ask:
1. are sessions always non-overlapping?
2. can they be unsorted? should we sort first?
3. what if only 1 session?

Plan in plain english:
sort the sessions by start time. loop from second session to end, convert start and end times to minutes, calculate gap between previous end and current start, keep track of minimum gap
"""

def conv(t):
 return t//100*60+t%100

def find_smallest_gap(sessions):
 if len(sessions)<2: return 0
 s = sorted(sessions,key=lambda x:x[0])
 min_gap = 99999
 for i in range(1,len(s)):
  g = conv(s[i][0])-conv(s[i-1][1])
  if g<min_gap: min_gap=g
 return min_gap

work_sessions = [(900,1100),(1300,1500),(1600,1800)]
print(find_smallest_gap(work_sessions))
work_sessions_2 = [(1000,1130),(1200,1300),(1400,1500)]
print(find_smallest_gap(work_sessions_2))
work_sessions_3 = [(900,1100),(1115,1300),(1315,1500)]
print(find_smallest_gap(work_sessions_3))

#time complexity: O(n log n)
#space complexity: O(n)
