"""
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.
"""
def pivot_index(nums):
    for i in range(len(nums)-1):
        if sum(nums[:i])==sum(nums[i+1:]):
            return i
    if 0==sum(nums[:-1]):
        return len(nums)-1
    return -1
nums =[1,2,3]
print(pivot_index(nums))