
"""
Questions I would ask to help understand question:


Plan in plain English (pseudocode):
We know that largest square is on left or right. Use two pointer until we reach the center finding the values of the highest absolute value
take those values and add their squares in order to a stack. Empty out the stack in order to reverse it (or just reverse using Python)

Begin problem:
"""

def engagement_boost(engagements):
    n = len(engagements)
    result = [0] * n
    left, right = 0, n - 1
    pos = n - 1
    
    while left <= right:
        if abs(engagements[left]) > abs(engagements[right]):
            result[pos] = engagements[left] ** 2
            left += 1
        else:
            result[pos] = engagements[right] ** 2
            right -= 1
        pos -= 1
    
    return result

print(engagement_boost([-4, -1, 0, 3, 10]))
print(engagement_boost([-7, -3, 2, 3, 11]))