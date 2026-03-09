class Solution:
    def isValid(self, s: str) -> bool:
        pMap = {
            ')' : '(',
            '}' : '{',
            ']' : '[',
        }
    
        stack = []
        #print(type(pMap), pMap)
        for ch in s:
            if ch in pMap:
                if len(stack) > 0:
                    #print('1 ', stack[-1])
                    #print('2 ', pMap[ch])
                    if stack[-1] == pMap[ch]:
                        stack.pop()
                    else:
                        stack.append(ch)
                else:
                    stack.append(ch)
            else:
                stack.append(ch)
            #print(stack)
        if len(stack) > 0:
            return False
        else:
            return True
