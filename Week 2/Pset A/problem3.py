"""
Questions I would ask to help understand question:
1. How do I iterate a dictionary?
2. How do I keep track of the sum?

Plan in plain English (pseudocode):
Iterate through all the keys of the dictionary and add the corresopnding values in a variable defined/initialized outside the loop.

Begin problem:
"""

def total_sales(ticket_sales):
    total = 0
    for key in ticket_sales:
        total += ticket_sales[key]
    return total 

# Example usage:
ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}

print(total_sales(ticket_sales))