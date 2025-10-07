class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        if len(s) == 0:
            return(s)

        for ch in s:
            if stack and stack[-1] == ch:
                stack.pop()
            else:
                stack.append(ch)

        print(stack)
        if len(stack) >= 0:
            return(''.join(stack))
        else:
            return('')





                