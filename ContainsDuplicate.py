"""
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.
"""
def contains_duplicates(nums):
    d=dict()
    for i in nums:
        if i not in d.keys():
            d.update({i:1})
        else:
            return True
    return False
