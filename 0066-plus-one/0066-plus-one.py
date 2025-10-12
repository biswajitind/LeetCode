class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = []
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            result.append((digits[i] + carry) % 10)
            carry = (digits[i] + carry) // 10
        
        if carry:
            result.append(1)

        result.reverse()
        return(result)


