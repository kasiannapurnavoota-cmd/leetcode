class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        r={}
        ordered_score=sorted(score,reverse=True)
        for i in range(len(ordered_score)):
            r[ordered_score[i]]=i+1
        res=[]
        for i in score:
            if r[i]==1:
                res.append("Gold Medal")
            elif r[i]==2:
                res.append("Silver Medal")
            elif r[i]==3:
                res.append("Bronze Medal")
            else:
                res.append(str(r[i]))
        return res
            