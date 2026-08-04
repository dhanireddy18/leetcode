class Solution:
    
    def isHappy(self,n: int) -> bool:
        s = set()
        while n>0:
            sum=0
            while n>0:
                d=n%10
                sum+=d**2
                n=n//10
            if sum==1:
                return True
            if sum in s:
                return False
            s.add(sum)
            n=sum