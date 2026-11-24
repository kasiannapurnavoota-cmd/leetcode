class Solution:
    def maxLength(self, nums: List[int]) -> int:
        from math import gcd,lcm,prod
        
        r=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)+1):
                k=nums[i:j]
                if prod(k)==lcm(*k) * gcd(*k)  and len(k)>r:
                    r=len(k)
        return r
                    