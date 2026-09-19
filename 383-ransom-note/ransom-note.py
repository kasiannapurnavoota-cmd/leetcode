class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r={}
        m={}
        for i in ransomNote:
            if i in r:
                r[i]+=1
            else:
                r[i]=1
        
        for i in magazine:
            if i in m:
                m[i]+=1
            else:
                m[i]=1
        if len(r)>len(m):
            return False
        for i in r:
            if i not in m:
                return False
            if r[i]>m[i]:
                return False
        return True
