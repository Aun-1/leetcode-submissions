class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)

        count = 0
        for n in nums:
            if n!=0:
                count+=1

        k = 0

        for i, n in enumerate(nums):
            if nums[i]!= 0:
                nums[k]=nums[i]
                k+=1

        for i in range(count,length):
            nums[i]=0
            
        return nums