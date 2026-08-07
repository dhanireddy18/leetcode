class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        nums=int("".join(list(map(str,digits))))+1
        narr=[]
        for i in str(nums):
            narr.append(int(i))
        return narr
        
        