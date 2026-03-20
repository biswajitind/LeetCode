class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        # For simplicity lets break down different outcomes in two categories.
        # 1. when all elements starting from 0 till i sums up to k 
        #    This means the current prefixSum == k
        # 2. irrespective of wheather current prefixSum equals to k or not, we have another scenerio
        #    which is, taking a sub array out from the beginning makes it equal to k
        #    in other words cSum - k is a prefixSum that we have already encountered before.
        #    This is where the hash lookup works.
        #    when we have negative values, we may get same prefixSum more than once as the sum increases as well as 
        #    descreases.
        #    This is why we store the count of prefixSum.
        #    The count against the prefixSum in the hash is, The number of different ways ( different subarrays ) 
        #    that can be taken out to make the sum equal to k

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