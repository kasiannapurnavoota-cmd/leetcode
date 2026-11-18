class Solution:
    def digitSum(self, s: str, k: int) -> str:
        
        while len(s)>k:
            su=0
            dup_li=[]
            for i in range(len(s)):
                su+=int(s[i])
                if (i+1)%k==0:
                    dup_li.append(str(su))
                    su=0
            if len(s)%k!=0:
                dup_li.append(str(su))
            s = "".join(dup_li)
        return s
                
        