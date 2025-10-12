class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # result = []
        # carry = 1
        # for i in range(len(digits) - 1, -1, -1):
        #     result.append((digits[i] + carry) % 10)
        #     carry = (digits[i] + carry) // 10
        
        # if carry:
        #     result.append(1)

        # result.reverse()
        # return(result)

        # No additional Space
        add_val = 1
        for i in range(len(digits) - 1, -1, -1):
            res = digits[i] + add_val
            add_val = res // 10
            digits[i] = res % 10
        
        if add_val:
            digits.reverse()
            digits.append(1)
            digits.reverse()
        return(digits)
