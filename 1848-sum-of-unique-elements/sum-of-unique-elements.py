class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        c=0
        s=set(nums)
        for i in s:
            if nums.count(i)==1:
                c+=i
        return c