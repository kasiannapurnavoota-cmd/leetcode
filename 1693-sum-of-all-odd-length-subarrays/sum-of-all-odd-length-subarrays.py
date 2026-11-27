class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        res=0
    
        for i in range(len(arr)):
            for j in range(i+1,len(arr)+1):
                l=len(arr[i:j])
                if l%2!=0:
                    res+=sum(arr[i:j])
        return res