class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result = []
        for i in range( max(len(a), len(b)) ):
            a_ind = len(a) - 1 - i
            b_ind = len(b) - 1 - i

            a_digit = int(a[a_ind]) if a_ind >= 0 else 0
            b_digit = int(b[b_ind]) if b_ind >= 0 else 0

            s = a_digit + b_digit + carry 
            result.append(s % 2)
            carry = s // 2
        if carry:
            result.append(1)
        
        result.reverse()
        result = [str(x) for x in result]
        return("".join(result))

