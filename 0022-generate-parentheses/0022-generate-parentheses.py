class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        stack = []

        # if open=close (open < n )we can only add (
        # if open>close 
            #add open if its still less than n
            # add close if its still less than n

        def _helper(openP=0, closeP=0):
            if openP == n and closeP == n:
                result.append(''.join(stack))
                return()
            if openP == closeP and openP < n:
                stack.append('(')
                _helper(openP+1, closeP)
                stack.pop()
            elif openP > closeP:
                if openP < n:
                    stack.append('(')
                    _helper(openP+1, closeP)
                    stack.pop()
                if closeP < n:
                    stack.append(')')
                    _helper(openP, closeP+1)
                    stack.pop()
            else:
                print("Error", openP, closeP)
        
        _helper()
        return(result)



            
            



