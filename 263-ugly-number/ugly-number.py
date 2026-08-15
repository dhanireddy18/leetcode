class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        prime_factor = [2,3,5]    
        for factor in prime_factor:
            while n%factor == 0:
                n //= factor
        return n == 1
                    