class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = 0
        for n in nums:
            if n != 0:
                nums[k] = n
                k += 1
        for i in range(k, len(nums)):
            nums[i] = 0