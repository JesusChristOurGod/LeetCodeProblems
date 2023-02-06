def search(nums, target):
    l = len(nums)
    indices = [x for x in range(l)]
    while True:
        p = len(nums)//2
        if len(nums)==1:
            return indices[0] if nums[0]==target else -1
        else:
            if nums[p]<target:
                nums = nums[p:]
                indices=indices[p:]
            elif nums[p]>target:
                nums = nums[:p]
                indices=indices[:p]
            else:
                return indices[len(indices)//2]
a =[5]
print(search(a, 5))