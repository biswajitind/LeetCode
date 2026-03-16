class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:

        for i in range(n):
            nums[i] += 10000 * nums[i + n]
        #print(nums)

        second = 2 * n - 1
        for i in range(n-1, -1, -1):
            nums[second] = nums[i] // 10000
            nums[second - 1] = nums[i] % 10000
            second -= 2

        return(nums)



