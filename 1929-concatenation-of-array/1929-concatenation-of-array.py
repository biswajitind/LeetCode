class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        size = len(nums)
        ans = [None] * 2 * size

        for i in range(size):
            ans[i] = ans[i + size] = nums[i]
        
        return(ans)