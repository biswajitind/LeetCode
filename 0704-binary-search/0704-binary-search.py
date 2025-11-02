class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # Edge case Note:
        # Since minimum number of elements in the list is 1 as per the Constrains, 
        # there is no need to ckeck for Null or Empty list as input.

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return(mid)
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        
        return(-1)