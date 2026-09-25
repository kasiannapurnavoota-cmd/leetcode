class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==1:
            return 1
        else:
            d={}
            for i in s:
                if i in d:
                    d[i]+=1
                else:
                    d[i]=1
            l=0
            for i in d:
                if d[i]%2==0:
                    l+=d[i]
                else:
                    l+=(d[i]-1)
                    d[i]=1
            for i in d.values():
                if i==1:
                    l+=1
                    break
            return l