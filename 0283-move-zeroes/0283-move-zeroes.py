class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        insert = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                if nums[insert] == 0:
                    #do nothing
                    pass
                else:
                    insert = i
            else:
                if nums[insert] == 0:
                    #swap
                    nums[insert], nums[i] = nums[i], nums[insert]
                    insert += 1

                

            


