
"""
Questions I would ask to help understand question:
1. What happens when the list has less than 3 numbers?
2. Are there negative numbers in the problem?

Plan in plain English (pseudocode):
Find minimum of list. Then find maximum of list. Iterate through list to find a nunmber that is neither the min or max. Return that number.

Begin problem:
"""
def goldilocks_approved(nums):
    if len(nums) < 3:
        return -1
    min_num = min(nums)
    max_num = max(nums)
    for num in nums:
        if num != min_num and num != max_num:
            return num
    return None


nums = [3, 2, 1, 4]
print(goldilocks_approved(nums))

nums = [1, 2]
print(goldilocks_approved(nums))

nums = [2, 1, 3]
print(goldilocks_approved(nums))
