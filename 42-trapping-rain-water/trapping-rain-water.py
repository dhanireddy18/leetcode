class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        water = 0
        lmax,rmax = 0,0
        while left<right:
            if height[left]<height[right]:
                lmax = max(height[left],lmax)
                water +=lmax-height[left]
                left += 1
            else:
                rmax = max(rmax,height[right])
                water += rmax-height[right]
                right -=1
        return water            


        