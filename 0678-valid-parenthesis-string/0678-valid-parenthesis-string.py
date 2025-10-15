class Solution:
    def checkValidString(self, s: str) -> bool:
        minP = 0
        maxP = 0
        for ch in s:
            if ch == '(':
                minP += 1
                maxP += 1
            elif ch == ')':
                minP -= 1
                maxP -= 1
            else:
                minP -= 1
                maxP += 1
            
            if maxP < 0:
                return(False)
            
            if minP < 0:
                minP = 0
                
        return(minP == 0)
