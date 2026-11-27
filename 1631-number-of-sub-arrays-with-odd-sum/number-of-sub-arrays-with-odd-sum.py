class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        a=[arr[0]]
        ec,oc,res=1,0,0
        if a[-1]%2==0:
            res+=oc
            ec+=1
        else:
            res+=ec
            oc+=1
        for i in range(1,len(arr)):
            a.append(a[-1]+arr[i])
            if a[-1]%2==0:
                res+=oc
                ec+=1
            else:
                res+=ec
                oc+=1
        return res % (10**9 + 7)