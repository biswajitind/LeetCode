class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        
        n = len(nums)
        result = []

        if len(nums) == 0:
            return([[lower, upper]])
        
        if nums[0] > lower:
            result.append([lower, nums[0] - 1])
        
        for i in range( n - 1):
            if nums[i] + 1 != nums[i+1]:
                result.append([nums[i] + 1, nums[i+1] -1 ])
                

        if nums[-1] < upper:
            result.append([nums[-1] + 1, upper])

        return(result)