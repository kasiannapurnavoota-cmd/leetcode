class Solution:
    def hasGroupsSizeX(self, deck: list[int]) -> bool:
        c={}
        from math import gcd
        for i in deck:
            if i in c:
                c[i]+=1
            else:
                c[i]=1
        
        
        a=[]
        for i in c.values():
           a.append(i)
        g=a[0]
        for i in range(1,len(a)):
            g=gcd(g,a[i])
        if g>=2:
            return True
        else:
            return False