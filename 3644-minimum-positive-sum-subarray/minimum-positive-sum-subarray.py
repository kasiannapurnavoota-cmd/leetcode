class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        le=len(nums)
        p=10000000
        for i in  range(le):
            for j in range(le-i):
                s=0
                ls=0
                for k in range(i,i+j+1):
                    s+=nums[k]
                    ls+=1
                if s>0 and l<=ls<=r:
                    p=min(s,p)
        if p==10000000:
            return -1
        return p


        