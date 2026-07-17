class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1738 ms Beats 19.35%
        # for i in range(len(nums) - 1):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return([i, j])
        visited = {}
        for i in range(len(nums)):
            if (target - nums[i]) in visited:
                return([i, visited[target - nums[i]]])
            else:
                visited[nums[i]] = i
        
        return([])
