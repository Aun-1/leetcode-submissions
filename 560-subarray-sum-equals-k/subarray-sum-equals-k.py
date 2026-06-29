class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = {0: 1}  # prefix sum -> number of times seen
        prefix_sum = 0
        result = 0
        for num in nums:
            prefix_sum += num
            # if (prefix_sum - k) has occurred before, that means
            # there's a subarray ending here that sums to k
            result += count.get(prefix_sum - k, 0)
            count[prefix_sum] = count.get(prefix_sum, 0) + 1
        return result