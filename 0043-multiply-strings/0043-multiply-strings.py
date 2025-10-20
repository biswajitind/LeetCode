class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        if '0' in [num1, num2]:
            return("0")


        num1, num2 = num1[::-1], num2[::-1]

        ans = [0] * (len(num1) + len(num2))
        carry = 0
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                ind = i1 + i2
                m = int(num1[i1]) * int(num2[i2]) + ans[ind]
                ans[ind+1] += m //10
                ans[ind] = m % 10

        
    
        
        while ans[-1] == 0:
            ans.pop()
        ans = ans[::-1]
        ans = [str(x) for x in ans]
        return(''.join(ans))
        
            

            


