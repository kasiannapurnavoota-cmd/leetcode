class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s=list(s)
        t=list(t)
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        e={}
        for i in t:
            if i in e:
                e[i]+=1
            else:
                e[i]=1
        t=list(set(t) )  
        for i in t:
            if i in d:
                if d[i]!=e[i]:
                    return str(i)
            else:
                return str(i)