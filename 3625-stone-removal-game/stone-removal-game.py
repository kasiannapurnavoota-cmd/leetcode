class Solution:
    def canAliceWin(self, n: int) -> bool:
        a,b=0,0
        i=10
        while n-i>=0:
            if i%2==0:
                a=1
                b=0
            else:
                b=1
                a=0
            n=n-i
            i-=1
        if a==1:
            return True
        return False
            
        