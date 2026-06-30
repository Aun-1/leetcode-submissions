class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainder_count = {0: 1}
        running_sum = 0
        ans = 0
        for n in nums:
            running_sum += n
            r = running_sum % k
            ans += remainder_count.get(r, 0)
            remainder_count[r] = remainder_count.get(r, 0) + 1
        return ans