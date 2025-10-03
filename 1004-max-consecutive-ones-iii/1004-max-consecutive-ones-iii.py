class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        right = 0
        left = 0
        curr = 0
        ans = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                curr += 1
            
            while curr > k:
                if nums[left] == 0:
                    curr -= 1
                left +=1 
            ans = max(ans, right - left + 1)
        return(ans)
