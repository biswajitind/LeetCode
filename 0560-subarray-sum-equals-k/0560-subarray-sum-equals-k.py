class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        cSum = 0
        result = 0
        prefixSum = {}
        for i in range(len(nums)):
            cSum += nums[i]
            if cSum == k:
                result += 1
            if (cSum - k) in prefixSum:
                result += prefixSum[cSum - k]
            
            if cSum in prefixSum:
                prefixSum[cSum] += 1
            else:
                prefixSum[cSum] = 1

        return(result)






        