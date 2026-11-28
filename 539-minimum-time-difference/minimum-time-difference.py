class Solution:
    def findMinDifference(self, timePoints: list[str]) -> int:
        t=[]
        
        for i in range(len(timePoints)):
            h,m=map(int,timePoints[i].split(":"))
            t.append(h*60+m)
        t.sort()
        res=(1440 - t[-1]) + t[0]
        for i in range(len(t)-1):
            res=min(res,t[i+1]-t[i])
        return res