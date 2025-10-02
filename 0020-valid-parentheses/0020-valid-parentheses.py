class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pmap = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []
        for i in range(len(s)):
            if s[i] in pmap.values():
                stack.append(s[i])
            else:
                if stack:
                    if pmap[s[i]] == stack[-1]:
                        stack.pop()
                    else:
                        return(False)
                    
                else:
                    return(False)
        if stack:
            return(False)
        
        return(True)
