"""
Given an integer array nums sorted in non-decreasing order,
return an array of the squares of each number sorted in non-decreasing order.
"""
#FIX
def sorted_squares(nums):
    res=[]
    for i in range((len(nums)//2)+1):
        j = len(nums)-i-1
        if i==j:
            res.append(nums[i]**2)
            continue
        if abs(nums[i])>abs(nums[j]):
            res.append(nums[i]**2)
            res.append(nums[j]**2)
        else:
            res.append(nums[j] ** 2)
            res.append(nums[i] ** 2)

    res.reverse()
    return res


print(sorted_squares([-5,-3,-2,-1]))