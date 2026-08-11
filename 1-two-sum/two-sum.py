class Solution:
    def twoSum(self, nums, target):
        dic={}
        cur=0
        for i in range(len(nums)):
            cur =target -nums[i]
            if cur in dic:
                return [dic[cur],i]
            else:
                dic[nums[i]]=i



