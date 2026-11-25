class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        a=[]
        a.append(-1)
        arr=arr[::-1]
        ma=arr[0]
        for i in range(1,len(arr)):
            ma=max(arr[i-1],ma)
            a.append(ma)
        a=a[::-1]
        return a