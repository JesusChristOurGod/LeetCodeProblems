def running_sum(nums):
    return [sum(nums[:i]) for i in range(1,len(nums)+1)]

