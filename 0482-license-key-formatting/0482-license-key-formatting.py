class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        result = "" 

        idx = len(s) - 1
        k1 = k
        while idx >= 0:
            # take the idx character which we have started from end and add to result
            if s[idx] != '-':
                if k1 <= 0:
                    result = "-" + result
                    k1 = k - 1
                else:
                    k1 -= 1
                result = s[idx] + result 

            idx -= 1
        return(result.upper())





        
        





        

