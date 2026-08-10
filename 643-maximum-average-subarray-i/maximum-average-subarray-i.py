class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cs = sum(nums[:k])
        ms = cs
        for i in range(k,len(nums)):
            cs += nums[i] - nums[i-k]
            ms = max(ms,cs)
        return ms/k    
        