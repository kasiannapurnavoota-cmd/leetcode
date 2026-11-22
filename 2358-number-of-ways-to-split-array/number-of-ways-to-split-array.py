class Solution(object):
    def waysToSplitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p=[]
        p.append(nums[0])
        for i in range(1,len(nums)):
            p.append(p[-1]+nums[i])
        s=[]
        r=nums[::-1]
        s.append(r[0])
        for i in range(1,len(r)):
            s.append(s[-1]+r[i])
        s=s[::-1]
        c=0
        for i in range(len(p)-1):
            if p[i]>=s[i+1]:
                c+=1
        return c
