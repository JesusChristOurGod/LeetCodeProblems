"""
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].
"""
def shuffle(nums, n):
    res=[]
    left = nums[:n]
    right = nums[n:]
    for i in range (n):
        res.append(left[i])
        res.append(right[i])
    return res

print(shuffle([2,5,1,3,4,7], 3))