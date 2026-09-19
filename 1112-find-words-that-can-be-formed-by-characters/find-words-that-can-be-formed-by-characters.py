class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        c={}
        for i in chars:
            if i in c:
                c[i]+=1
            else:
                c[i]=1
        res=0
        for i in words:
            co=0
            for char in i:
                if char in c and c[char]>=i.count(char):
                    co+=1
            if co==len(i):
                res+=co
        return res