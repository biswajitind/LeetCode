class Solution:
    def decodeString(self, s: str) -> str:            
        stack = []

        for i in range(len(s)):
            if s[i] == "]":
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr

                # pop the '['
                stack.pop()
                
                # now pop the digits if we have any
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k) * substr)
            
            else:
                stack.append(s[i])
        
        return("".join(stack))
