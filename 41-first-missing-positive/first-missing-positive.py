class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #problem: TC->O(n^2)
        # result=1
        # idx=0
        # while idx<len(nums):
        #     if nums[idx]==result:
        #         result+=1
        #         idx=-1
        #     idx+=1
        # return result
        
        size = len(nums)

        for i in range(size):
            n = nums[i]
            while 1 <= n <= size and n != (i + 1) and n != nums[n - 1]:
                nums[i], nums[n - 1] = nums[n - 1], nums[i]
                n = nums[i]

        for i in range(size):
            if nums[i] != (i + 1):
                return i + 1

        return size + 1