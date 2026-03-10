class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chrSet = set()
        maxLen = 0
        left = 0
        for i in range(len(s)):
            while s[i] in chrSet:
                chrSet.discard(s[left])
                left += 1
            maxLen = max(maxLen, i + 1 - left)
            chrSet.add(s[i])
        return(maxLen)

