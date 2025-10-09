class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        # simple iteration. Initial thought.        
        # for c in letters:
        #     if c > target:
        #         return(c)
        # return(letters[0])

        # Binary search
        l = 0
        r = len(letters) - 1

        # default return value
        val = letters[0]
        while l <= r:
            m = (l + r) // 2
            if letters[m] <= target:
                l = m+1
            else:
                val = letters[m]
                r = m-1
        return(val)
                

        