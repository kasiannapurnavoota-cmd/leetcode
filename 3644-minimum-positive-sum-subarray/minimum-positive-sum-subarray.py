class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        
        min_sum = 100000000
        n = len(nums)
        
        for i in range(n):
            current_sum = 0
            for j in range(i, n):
                current_sum += nums[j]
                length = j - i + 1
                
                if l <= length <= r and current_sum > 0:
                    min_sum = min(min_sum, current_sum)
                    
        return min_sum if min_sum != 100000000 else -1            

        