class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        # shotcuts
        if len(needle) > len(haystack):
            return(-1)

        # Sliding window
        i = 0 # haystack index
        j = 0 # needle index
        while i <= len(haystack) - len(needle):
            print('while', i)
            startInd = i
            match = True
            for j in range(len(needle)):
                print('for', j)
                if haystack[i] == needle[j]:
                    j += 1
                    i += 1
                else:
                    match = False
            if match:
                return(startInd)

            i = startInd + 1

        return(-1)