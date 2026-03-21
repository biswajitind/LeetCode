class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        print('I', nums)
        # Remove negatives
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        print('Z', nums)

        # check and set -ve
        for i in range(len(nums)):
            val = abs(nums[i])
            if val > 0:
                pos = val - 1
                if pos < len(nums):
                    if nums[pos] == 0:
                        nums[pos] = (len(nums) + 1) * -1
                    else:
                        nums[pos] = abs(nums[pos]) * -1
                    

        print('N', nums)

        for i in range(1, len(nums) + 1):
            if not nums[i-1] < 0:
                return(i)
        return(len(nums) + 1)
        


        