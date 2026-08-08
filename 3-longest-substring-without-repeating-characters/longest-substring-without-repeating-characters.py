class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i,j = 0,0
        mlength = 0
        seen = set()
        while j<len(s):
            while s[j] in seen:
                seen.remove(s[i])
                i = i+ 1
            seen.add(s[j])
            length = j-i+1
            mlength = max(mlength,length)
            j = j+1
        return mlength        
            

        