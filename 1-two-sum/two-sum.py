class Solution:
    def twoSum(self, nums, target):
        arr=[]

        for i,v in enumerate(nums):
            for j in range(i+1,len(nums)):

                 if nums[j]+v==target:
                    arr.append(i)

                    arr.append(j)
                    return arr
        return arr