"""
Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""
def searchInsert(nums, target):
    for i in range(len(nums)-1):
        if nums[i]<target<=nums[i+1]:
            return i+1
        if nums[i]==target:
            return i
    return len(nums) if target>nums[len(nums)-1] else 0
print(searchInsert(nums = [1,3,5,6], target = 7))