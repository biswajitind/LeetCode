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
        for c in s:
            if c in pmap:
                if stack and stack[-1] == pmap[c]:
                    stack.pop()
                else:
                    return(False)
            else:
                stack.append(c)
        return False if stack else True

