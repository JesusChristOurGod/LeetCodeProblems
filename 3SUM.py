#FIX
class Solution:
    def threeSum(self, nums):
        nums.sort()
        res=[]
        for i in range(len(nums)//3):
            start = nums[0]
            end = nums[-1]
            nums.pop(0)
            nums.pop(-1)
            for j in range(len(nums)):
                if start+end+nums[j]==0:
                    res.append((start, end,nums[j]))
                    nums.pop(j)
        return(set(res))



a=Solution()
nums = [-1,0,1,2,-1,-4]
print(a.threeSum(nums))