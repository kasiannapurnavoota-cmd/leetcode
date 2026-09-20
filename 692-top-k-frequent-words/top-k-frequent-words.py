class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        d={}
        for i in words:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        a=sorted(d,key=lambda x: (-d[x], x))
        return a[:k]