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
            has_odd=False
            for count in d.values():
                l += count // 2 * 2
                if count % 2 == 1:
                    has_odd = True
            
            return l + 1 if has_odd else l