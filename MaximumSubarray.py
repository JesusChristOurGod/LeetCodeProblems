"""
Given an integer array nums, find the
subarray
 with the largest sum, and return its sum.
"""
def max_subarray(nums):
    best_sum = float('-inf')
    current_sum = 0
    for x in nums:
        current_sum = max(x, current_sum + x)
        best_sum = max(best_sum, current_sum)
    return best_sum




nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray(nums))