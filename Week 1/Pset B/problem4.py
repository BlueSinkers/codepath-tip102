
"""
Questions I would ask to help understand question:
1. Can I convert to integer and do this the string method?
2. What do I do for single digit numbers?

Plan in plain English (pseudocode):
Divide each nunber by 10 and get remainder. Add remainder to number until number is 0. Return the sum.

Begin problem:
"""
def sum_of_digits(num):
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total

num = 423
print(sum_of_digits(num))

num = 4
print(sum_of_digits(num))
