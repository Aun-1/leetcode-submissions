class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainder_count = {0: 1}
        total = 0
        ans = 0
        for n in nums:
            total += n
            r = total % k          # Python's % always returns non-negative for positive k
            ans += remainder_count.get(r, 0)
            remainder_count[r] = remainder_count.get(r, 0) + 1
        return ans