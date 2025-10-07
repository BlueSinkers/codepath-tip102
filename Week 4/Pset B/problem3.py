"""
Questions I would ask:
1. can a category appear only once?
2. what if the list is empty?

Plan in plain english:
loop through expenses, sum amounts per category in a dictionary, after loop find category with max total, return dictionary and category with highest total
"""

def calculate_expenses(exp):
 totals = {}
 for c,a in exp: totals[c] = totals.get(c,0)+a
 maxcat = max(totals,key=totals.get) if totals else None
 return totals,maxcat

expenses = [("Food",12.5),("Transport",15.0),("Accommodation",50.0),
            ("Food",7.5),("Transport",10.0),("Food",10.0)]
print(calculate_expenses(expenses))

expenses_2 = [("Entertainment",20.0),("Food",15.0),("Transport",10.0),
              ("Entertainment",5.0),("Food",25.0),("Accommodation",40.0)]
print(calculate_expenses(expenses_2))

expenses_3 = [("Utilities",100.0),("Food",50.0),("Transport",75.0),
              ("Utilities",50.0),("Food",25.0)]
print(calculate_expenses(expenses_3))

#time complexity: O(n)
#space complexity: O(k)
