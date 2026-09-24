def sm(n):
    s=0
    while n>0:
        s+=n%10
        n=n//10
    return s
class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            if sm(nums[i])==i:
                return i
        return -1
