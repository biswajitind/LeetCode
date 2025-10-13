class Solution:
    def hammingWeight(self, n: int) -> int:

        # Solution 1
        # ans = 0
        # while n != 0:
        #     ans += 1
        #     n = n & (n-1)
        # return(ans)

        # Solution 2
        count = 0
        while n >= 1:
            if (n % 2) == 1:
                count += 1
            n = n // 2
        if n:
            count += 1
        return(count)