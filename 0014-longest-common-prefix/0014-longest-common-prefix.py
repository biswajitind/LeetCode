class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minLen = float('inf')

        for s in strs:
            minLen = min(minLen, len(s))

        i = 0
        while i < minLen:
            for s in strs:
                if s[i] != strs[0][i]:
                    return(s[:i])
            i += 1

        return(s[:i])