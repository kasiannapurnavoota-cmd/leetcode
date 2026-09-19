class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        
        p=["!","?",",",".",";","'"]
        d={}
        for char in p:
            paragraph = paragraph.replace(char, " ")
        a=paragraph.split()
        for i in a:
            l=len(i)
            i=i.lower()
            if i not in banned:

                if i in d:
                    d[i]+=1
                else :
                    d[i]=1
        m=max(d.values())
        for i in d:
            if d[i]==m :
                return i