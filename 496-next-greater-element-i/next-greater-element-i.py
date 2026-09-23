class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d={}
        for i in range(len(nums2)-1):
            c=[]
            
            for j in range(i+1,len(nums2)):
                if nums2[j]>nums2[i]:
                    c.append(nums2[j])
                    break
            d[nums2[i]]=c
        ans=[]
        for i in nums1:
            
            if i==nums2[-1]:
                ans.append(-1)
            elif len(d[i])==0:
                ans.append(-1)
            else:
                t=d[i]
                ans.append(t[0])
        return ans