class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        d={}
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]]+=1
            else:
                d[s[i]]=1
        a=sorted(d,key=d.get,reverse=True)
        c=""
        for i in a:
            for _ in range(d[i]):
                c+=i
        return c        