class Solution:
    def addDigits(self, num: int) -> int:
        
        while num >= 10:
            d_sum = 0
            while num > 0:
                d_sum += num%10
                num //=10
            num = d_sum    
        return num    
        