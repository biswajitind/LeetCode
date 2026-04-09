class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Two pointers
        res = ""
        idx = 0

        while idx < len(word1) and idx < len(word2):
            res += word1[idx]
            res += word2[idx]
            idx += 1

        if idx < len(word1):
            res += word1[idx:]
        if idx < len(word2):
            res += word2[idx:]

        return(res)