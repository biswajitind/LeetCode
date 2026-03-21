class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        h = set()
        for i in range(len(nums)):
            h.add(nums[i])
        
        for i in range(1, len(nums) + 1):
            if not i in h:
                return(i)
        return(len(nums) + 1)

