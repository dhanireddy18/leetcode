class Solution:
    def intToRoman(self, num: int) -> str:
        values = [(1,'I'),(4,'IV'),(5,'V'),(9,'IX'),(10,'X'),(40,'XL'),(50,'L'),(90,'XC'),(100,'C'),(400,'CD'),(500,'D'),(900,'CM'),(1000,'M')]
        #900:'CM',400:'CD',40:'XL',9:'IX',90:'XC'
        result = ""
        for i,j in values[::-1]:
            while num >= i:
                result += j
                num -= i
        return result        

        
        