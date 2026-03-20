class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        size = len(nums)

        # Simple solution 1
        # ans = [None] * 2 * size
        # for i in range(size):
        #     ans[i] = ans[i + size] = nums[i]        
        # return(ans)

        #reusing the input array to save space
        for i in range(size):
            nums.append(nums[i])
        return(nums)