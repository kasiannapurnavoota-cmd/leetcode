class Solution:
    def countDominantElements(self, nums: list[int]) -> int:
        n=len(nums)
        c=0
        if n==1:
            return 1
        else:
            for i in range(1,len(nums)-1):
                av=(nums[i-1]+nums[i+1])/2
                if nums[i]>=av:
                    c+=1
            if nums[0]>=nums[1]: c+=1
            if nums[-1]>=nums[-2]: c+=1
            return c
