class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        nums.sort()
        left = 0
        window_sum = 0
        best = 1
        for right in range(len(nums)):
            window_sum += nums[right]
            '''
If I want to make [1, 2, 4] all equal to 4...
cost = (4-1) + (4-2) + (4-4)
     = 4×3 - (1+2+4)
     = target × window_size - window_sum
            '''
            while nums[right] * (right - left + 1) - window_sum > k:
                window_sum -= nums[left]
                left += 1
            best = max(best, right - left + 1)
        return best