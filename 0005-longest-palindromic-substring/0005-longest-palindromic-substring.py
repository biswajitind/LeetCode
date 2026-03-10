class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = s[0]
        resultLen = 1

        for i in range(len(s)):
            # odd length
            l, r = i -1, i+1 
            while l >=0 and r < len(s) and s[l] == s[r]:
                cLen = r - l + 1
                if cLen > resultLen:
                    result = s[l:r+1]
                    resultLen = max(resultLen, cLen)
                l -= 1
                r += 1
            
            # even length
            l, r = i, i+1 
            while l >=0 and r < len(s) and s[l] == s[r]:
                cLen = r - l + 1
                if cLen > resultLen:
                    result = s[l:r+1]
                    resultLen = max(resultLen, cLen)
                l -= 1
                r += 1
        return(result)

