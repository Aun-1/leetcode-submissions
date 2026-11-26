class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        if sum(nums)<target:
            return 0
        
        length = len(nums)
        left = 0
        total = 0
        for right in range(len(nums)):
            total += nums[right]                        # ADD
            while total >= target:                      # still valid → try shorter
                length = min(length, right - left + 1)  # MEASURE inside the loop
                total -= nums[left]                     # SHRINK
                left += 1
        return length