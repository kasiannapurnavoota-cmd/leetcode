
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        a=[]
        while True:
            ans=0
            while n>0:
                l=n%10
                ans+=l**2
                n=n//10
            if ans==1:
                return True
            if ans in a:
                return False
            a.append(ans)
            n=ans


    
    
        