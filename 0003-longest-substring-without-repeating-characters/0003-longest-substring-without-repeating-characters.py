class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return(0)
        
        map = {}
        left = longest = 0
        for r, c in enumerate(s):
            if c in map:
                left = max(left, map[c] + 1)
            
            longest = max(longest, (r - left + 1))
            map[c] = r    
        return(longest)    
        
