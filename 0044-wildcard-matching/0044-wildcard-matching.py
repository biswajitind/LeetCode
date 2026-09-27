class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        # Optimization. Reduce the patterns by eliminating duplicate *
        new_p = ''

        for ch in p:
            if ch != '*' or (not new_p) or (new_p and new_p[-1] != '*'):
                new_p += ch

        p = new_p

        sLen = len(s)
        pLen = len(p)

        memo = [ [False] * (pLen + 1) for _ in range(sLen + 1)]

        if sLen + pLen == 0:
            return(True)

        if pLen == 0:
            return(False)

        if sLen == 0 and pLen == 1 and p[0] == '*':
            return(True)
        
        memo[0][0] = True

        if p[0] == '*':
            memo[0][1] = True

        for m in range(1, sLen +1):
            for n in range(1, pLen + 1):
                if s[m-1] == p[n-1] or p[n-1] == '?':
                    memo[m][n] = memo[m-1][n-1]
                if p[n-1] == '*':
                    memo[m][n] = memo[m-1][n] or memo[m][n-1]
        
        return(memo[sLen][pLen])
                


        


            