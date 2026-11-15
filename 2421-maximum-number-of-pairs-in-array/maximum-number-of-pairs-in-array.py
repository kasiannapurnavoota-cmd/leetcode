class Solution:
    def numberOfPairs(self, nums: list[int]) -> list[int]:
        s=list(set(nums))
        a,b=0,0
        for i in s:
            a+=(nums.count(i)//2)
            b+=(nums.count(i)%2)
        return [a,b]
