class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # nums=int("".join(list(map(str,digits))))+1
        # narr=[]
        # for i in str(nums):
        #     narr.append(int(i))
        # return narr


        # if digits[-1]<9:
        #      digits[-1]+=1
        #      return digits
        # else:
        #     carry=1
        #     for i in range(len(digits)-1,-1,-1):
        #         if digits[i]==9 and carry==1:
        #             digits[i]=0
        #             carry=1
        #         else:
        #             s=digits[i]+carry
        #             if s>9:
        #                 digits[i]=0
        #                 carry=1
        #             else:
        #                 digits[i]=s
        #                 carry=0
        # if carry==1:
        #     digits.insert(0,1)
        # return digits


        n = len(digits)
        for i in range(n-1,-1,-1):
            if digits[i]<9:
                digits[i]+=1
                return digits
            else:
                digits[i] = 0
        return [1]+digits                



        
        