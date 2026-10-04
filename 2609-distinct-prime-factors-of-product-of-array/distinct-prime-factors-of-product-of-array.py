class Solution:
    def distinctPrimeFactors(self, nums: list[int]) -> int:
        prime_factors = set()
    
        for num in nums:
        # Check divisibility starting from 2
            d = 2
            while d * d <= num:
                if num % d == 0:
                    prime_factors.add(d)
                # Divide out all occurrences of this factor
                    while num % d == 0:
                        num //= d
                d += 1
        
        # If the remaining number is greater than 1, it is prime
            if num > 1:
                prime_factors.add(num)
            
        return len(prime_factors)