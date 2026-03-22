class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        
        # since
        longest = 0

        for n in numSet:
            if not n - 1 in numSet:
                cLen = 0
                while n + cLen in numSet:
                    cLen += 1
                longest = max(longest, cLen)
        return(longest)


        