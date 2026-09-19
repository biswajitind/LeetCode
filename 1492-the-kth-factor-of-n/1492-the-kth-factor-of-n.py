class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        # Since its kth Factor, we will use a heap.
        # we dont need a heap, we can simply loop and stop at k  
        # Lets start with a simple logic by starting from 1

        factor = 1
        f = 1
        count = 1
        while f <= n and count < k:
            f = f + 1
            if n % f == 0:
                factor = f
                count += 1
        
        if count == k:
            return(factor)
        else:
            return( -1 )



